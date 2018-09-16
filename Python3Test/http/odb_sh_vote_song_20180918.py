#!/usr/bin/env python3
# coding=utf-8


import requests
import time
import os
# import uuid
import re


class Vote(object):
    def __init__(self, keyId):
        self.keyId = keyId
        self.voteCount = 0
        self.totalCount = 'unknown'
        self.errorResult = ''

    def vote(self):
        while self.voteCount < 15:
            result = self.do_vote()
            if result.find('本日投票次数已满') >= 0:
                break
            elif result.find('投票成功') >= 0:
                print(result)
                self.voteCount += 1
                obj = re.search('票数：(.+?)</p>', result)
                self.totalCount = obj.group(1)
                time.sleep(3)
            else:
                self.voteCount += 1
                print('未知的结果:' + result)
                self.errorResult = result
                break

    def do_vote(self):
        payload = {'keyId': self.keyId, 'type': 'detail'}
        response = requests.post('http://dev.odb.sh.cn/xsd/clientVote', payload)
        return response.text

    def do_vote_mock(self):
        if self.voteCount < 10:
            result = '<p class="piaoNum2">票数：11,603</p>\n<input type="hidden" id="i_message" value="投票成功" />'
        else:
            result = '<input type="hidden" id="i_message" value="本日投票次数已满" />'
        return result


def append_log_to_file(_filename, _msg):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    fo = open(_filename, "a")
    # fo.seek(0, 2)
    fo.write(_msg + '\n')
    fo.close()


if __name__ == "__main__":
    filename = '../logs/http/odb_sh_vote_song_' + time.strftime("%Y%m%d%H%M%S", time.localtime()) + '.txt'
    print('filename=' + filename)
    voteCount = 0
    try:
        while True:
            # keyId = uuid.uuid4()
            keyId = 'f5a38c75-4a3d-4368-bf89-7bd48f52cb73'  # 每个视频不同的id
            vote = Vote(keyId)
            vote.vote()
            voteCount += vote.voteCount
            msg = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) \
                  + f': 一轮投票结束，当前自己共投票{voteCount}, 页面共{vote.totalCount}票'
            print(msg)
            append_log_to_file(filename, msg)
            if len(vote.errorResult) > 0:
                append_log_to_file(filename, vote.errorResult)
                break
            time.sleep(30)
    except KeyboardInterrupt:
        pass
