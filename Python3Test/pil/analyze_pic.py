#!/usr/bin/env python3
# coding=utf-8

from PIL import Image, ImageDraw
import os
import time
import math

under_game_score_y = 200
piece_base_height_1_2 = 13
piece_body_width = 49


def find_piece_and_board(im):
    w, h = im.size

    print("size: {}, {}".format(w, h))

    piece_x_sum = piece_x_c = piece_y_max = 0
    board_x = board_y = 0
    scan_x_border = int(w / 8)  # 扫描棋子时的左右边界
    scan_start_y = 0  # 扫描的起始 y 坐标
    im_pixel = im.load()

    # 以 50px 步长，尝试探测 scan_start_y
    for i in range(under_game_score_y, h, 50):
        last_pixel = im_pixel[0, i]
        for j in range(1, w):
            pixel = im_pixel[j, i]

            # 不是纯色的线，则记录scan_start_y的值，准备跳出循环
            if pixel != last_pixel:
                scan_start_y = i - 50
                break

        if scan_start_y:
            break

    print("scan_start_y: ", scan_start_y)

    # 从 scan_start_y 开始往下扫描，棋子应位于屏幕上半部分，这里暂定不超过 2/3
    for i in range(scan_start_y, int(h * 2 / 3)):
        # 横坐标方面也减少了一部分扫描开销
        for j in range(scan_x_border, w - scan_x_border):
            pixel = im_pixel[j, i]
            # 根据棋子的最低行的颜色判断，找最后一行那些点的平均值，这个颜
            # 色这样应该 OK，暂时不提出来
            if (50 < pixel[0] < 60) \
                    and (53 < pixel[1] < 63) \
                    and (95 < pixel[2] < 110):
                piece_x_sum += j
                piece_x_c += 1
                piece_y_max = max(i, piece_y_max)
                im.putpixel([j, i], (255, 0, 0))

    if not all((piece_x_sum, piece_x_c)):
        return 0, 0, 0, 0
    piece_x = piece_x_sum / piece_x_c
    piece_y = piece_y_max - piece_base_height_1_2  # 上移棋子底盘高度的一半

    for i in range(int(h / 3), int(h * 2 / 3)):
        last_pixel = im_pixel[0, i]
        if board_x or board_y:
            break
        board_x_sum = 0
        board_x_c = 0

        for j in range(w):
            pixel = im_pixel[j, i]
            # 修掉脑袋比下一个小格子还高的情况的 bug
            if abs(j - piece_x) < piece_body_width:
                continue

            # 修掉圆顶的时候一条线导致的小 bug，这个颜色判断应该 OK，暂时不提出来
            if abs(pixel[0] - last_pixel[0]) \
                    + abs(pixel[1] - last_pixel[1]) \
                    + abs(pixel[2] - last_pixel[2]) > 10:
                board_x_sum += j
                board_x_c += 1

        if board_x_sum:
            board_x = board_x_sum / board_x_c

    # 按实际的角度来算，找到接近下一个 board 中心的坐标 这里的角度应该
    # 是 30°,值应该是 tan 30°, math.sqrt(3) / 3
    board_y = piece_y - abs(board_x - piece_x) * math.sqrt(3) / 3

    if not all((board_x, board_y)):
        return 0, 0, 0, 0

    return piece_x, piece_y, board_x, board_y


def save_debug_screenshot(oriFileName, im, piece_x, piece_y, board_x, board_y):
    # draw = ImageDraw.Draw(im)
    # draw.line((piece_x, piece_y) + (board_x, board_y), fill=2, width=3)
    # draw.line((piece_x, 0, piece_x, im.size[1]), fill=(255, 0, 0))
    # draw.line((0, piece_y, im.size[0], piece_y), fill=(255, 0, 0))
    # draw.line((board_x, 0, board_x, im.size[1]), fill=(0, 0, 255))
    # draw.line((0, board_y, im.size[0], board_y), fill=(0, 0, 255))
    # draw.ellipse((piece_x - 10, piece_y - 10, piece_x + 10, piece_y + 10), fill=(255, 0, 0))
    # draw.ellipse((board_x - 10, board_y - 10, board_x + 10, board_y + 10), fill=(0, 0, 255))
    # del draw
    splitTexts = os.path.splitext(oriFileName)
    im.save('{}_debug{}'.format(splitTexts[0], splitTexts[1]))


def main():
    oriFileName = "./jump_1.png"
    im = Image.open(oriFileName)

    # 获取棋子和 board 的位置
    piece_x, piece_y, board_x, board_y = find_piece_and_board(im)
    ts = int(time.time())
    print(ts, piece_x, piece_y, board_x, board_y)
    if piece_x == 0:
        return

    save_debug_screenshot(oriFileName, im, piece_x, piece_y, board_x, board_y)


if __name__ == '__main__':
    main()
