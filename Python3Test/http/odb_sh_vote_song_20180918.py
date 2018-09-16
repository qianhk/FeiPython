#!/usr/bin/env python3
# coding=utf-8


import requests
import time
import os
# import uuid
import re
import sys

# http://url.cn/5lQLOqg
# vote_url = 'http://dev.odb.sh.cn/xsd/clientVote'
# vote_url = 'http://httpbin.org/post'
# vote_url = 'http://httpbin.org/cookies'
vote_url = 'http://devjava.odb.sh.cn/xsd/clientVote'

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'


class Vote(object):
    def __init__(self, keyId):
        self.keyId = keyId
        self.voteCount = 0
        self.totalCount = 'unknown'
        self.errorResult = ''

    def vote(self):
        error_count = 0
        while self.voteCount < 10:
            result = self.do_vote()
            if result.find('本日投票次数已满') >= 0:
                break
            elif result.find('投票成功') >= 0:
                error_count = 0
                self.voteCount += 1
                obj = re.search('票数：(.+?)</p>', result)
                self.totalCount = obj.group(1)
                time.sleep(1)
            elif result.find('<title>404') >= 0 or result.find('<title>502') >= 0:
                print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ': found result has 404 or 502')
                time.sleep(60)
            else:
                print('未知的结果:' + result)
                error_count += 1
                if error_count > 12:
                    self.errorResult = result
                    break
                else:
                    time.sleep(5 * 60)

    def do_vote(self):
        payload = {'keyId': self.keyId, 'type': 'detail'}
        cookies = dict(systemCode='b4a53cf611e93955e79c9f5c1487992e')
        headers = {'User-Agent': USER_AGENT, 'Referer': vote_url}
        response = requests.post(vote_url, payload, cookies=cookies, headers=headers)
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
    pyfiledir = os.path.dirname(os.path.realpath(sys.argv[0])) + '/'
    # print('python file dir:' + pyfiledir)
    filename = pyfiledir + '../logs/http/odb_sh_vote_song_' + time.strftime("%Y%m%d%H%M%S", time.localtime()) + '.txt'
    filename = os.path.realpath(filename)
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
            time.sleep(5)
    except KeyboardInterrupt:
        pass
