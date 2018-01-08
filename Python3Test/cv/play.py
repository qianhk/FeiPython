# -*- coding:utf-8 -*-
# Created Time: 六 12/30 13:49:21 2017
# Author: Taihong Xiao <xiaotaihong@126.com>

import argparse
import glob
import os
import random
import shutil
import time

import cv2
import numpy as np


def multi_scale_search(pivot, screen, range=0.3, num=10):
    H, W = screen.shape[:2]
    h, w = pivot.shape[:2]

    found = None
    for scale in np.linspace(1 - range, 1 + range, num)[::-1]:
        resized = cv2.resize(screen, (int(W * scale), int(H * scale)))
        r = W / float(resized.shape[1])
        if resized.shape[0] < h or resized.shape[1] < w:
            break
        res = cv2.matchTemplate(resized, pivot, cv2.TM_CCOEFF_NORMED)

        loc = np.where(res >= res.max())
        pos_h, pos_w = list(zip(*loc))[0]

        if found is None or res.max() > found[-1]:
            found = (pos_h, pos_w, r, res.max())

    if found is None: return (0, 0, 0, 0, 0)
    pos_h, pos_w, r, score = found
    start_h, start_w = int(pos_h * r), int(pos_w * r)
    end_h, end_w = int((pos_h + h) * r), int((pos_w + w) * r)
    return [start_h, start_w, end_h, end_w, score]


class WechatAutoJump(object):
    def __init__(self, sensitivity, debug, resource_dir):
        self.sensitivity = sensitivity
        self.debug = debug
        self.resource_dir = resource_dir
        self.bb_size = [300, 300]
        self.step = 1
        self.load_resource()
        if self.debug:
            if not os.path.exists(self.debug):
                os.mkdir(self.debug)

    def load_resource(self):
        self.player = cv2.imread(os.path.join(self.resource_dir, 'player.png'), 0)
        circle_file = glob.glob(os.path.join(self.resource_dir, 'circle/*.png'))
        table_file = glob.glob(os.path.join(self.resource_dir, 'table/*.png'))
        self.jump_file = [cv2.imread(name, 0) for name in circle_file + table_file]

    def get_current_state(self):
        pic_filename = 'state{:03d}.png'.format(self.step)
        state = cv2.imread(pic_filename)
        self.resolution = state.shape[:2]
        scale = state.shape[1] / 720.
        state = cv2.resize(state, (720, int(state.shape[0] / scale)), interpolation=cv2.INTER_NEAREST)
        if state.shape[0] > 1280:
            s = (state.shape[0] - 1280) // 2
            state = state[s:(s + 1280), :, :]
        elif state.shape[0] < 1280:
            s1 = (1280 - state.shape[0]) // 2
            s2 = (1280 - state.shape[0]) - s1
            pad1 = 255 * np.ones((s1, 720, 3), dtype=np.uint8)
            pad2 = 255 * np.ones((s2, 720, 3), dtype=np.uint8)
            state = np.concatenate((pad1, state, pad2), 0)
        return state

    def get_player_position(self, state):
        state = cv2.cvtColor(state, cv2.COLOR_BGR2GRAY)
        pos = multi_scale_search(self.player, state, 0.3, 10)
        h, w = int((pos[0] + 13 * pos[2]) / 14.), (pos[1] + pos[3]) // 2
        return np.array([h, w])

    def get_target_position(self, state, player_pos):
        state = cv2.cvtColor(state, cv2.COLOR_BGR2GRAY)
        sym_center = [1280, 720] - player_pos
        sym_tl = np.maximum([0, 0], sym_center + np.array([-self.bb_size[0] // 2, -self.bb_size[1] // 2]))
        sym_br = np.array(
            [min(sym_center[0] + self.bb_size[0] // 2, player_pos[0]), min(sym_center[0] + self.bb_size[1] // 2, 720)])

        state_cut = state[sym_tl[0]:sym_br[0], sym_tl[1]:sym_br[1]]
        target_pos = None
        for target in self.jump_file:
            pos = multi_scale_search(target, state_cut, 0.4, 15)
            if target_pos is None or pos[-1] > target_pos[-1]:
                target_pos = pos
        return np.array([(target_pos[0] + target_pos[2]) // 2, (target_pos[1] + target_pos[3]) // 2]) + sym_tl

    def get_target_position_fast(self, state, player_pos):
        state_cut = state[:player_pos[0], :, :]
        m1 = (state_cut[:, :, 0] == 245)
        m2 = (state_cut[:, :, 1] == 245)
        m3 = (state_cut[:, :, 2] == 245)
        m = np.uint8(np.float32(m1 * m2 * m3) * 255)
        b1, b2 = cv2.connectedComponents(m)
        for i in range(1, np.max(b2) + 1):
            x, y = np.where(b2 == i)
            # print('fast', len(x))
            if len(x) > 280 and len(x) < 310:
                r_x, r_y = x, y
        h, w = int(r_x.mean()), int(r_y.mean())
        return np.array([h, w])

    def jump(self, player_pos, target_pos):
        distance = np.linalg.norm(player_pos - target_pos)
        press_time = distance * self.sensitivity
        press_time = int(press_time)

    def debugging(self):
        current_state = self.state.copy()
        cv2.circle(current_state, (self.player_pos[1], self.player_pos[0]), 5, (0, 255, 0), -1)
        cv2.circle(current_state, (self.target_pos[1], self.target_pos[0]), 5, (0, 0, 255), -1)
        cv2.imwrite(os.path.join(self.debug, 'state_{:03d}_res_h_{}_w_{}.png'.format(self.step, self.target_pos[0],
                                                                                     self.target_pos[1])),
                    current_state)

    def play(self):
        self.state = self.get_current_state()
        self.player_pos = self.get_player_position(self.state)
        try:
            self.target_pos = self.get_target_position_fast(self.state, self.player_pos)
            print('fast-search, step: %04d' % self.step)
        except UnboundLocalError:
            self.target_pos = self.get_target_position(self.state, self.player_pos)
            print('multiscale-search, step: %04d' % self.step)

        if self.debug:
            self.debugging()
        self.jump(self.player_pos, self.target_pos)
        self.step += 1
        time.sleep(1.5)

    def run(self):
        try:
            while True:
                self.play()
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--resource', default='resource', type=str, help='resource dir')
    parser.add_argument('--sensitivity', default=2.045, type=float, help='constant for press time')
    parser.add_argument('--debug', default=None, type=str,
                        help='debug mode, specify a directory for storing log files.')
    args = parser.parse_args()
    print(args)

    AI = WechatAutoJump(args.sensitivity, args.debug, args.resource)
    # AI.run()
    AI.play()
