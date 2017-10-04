#!/usr/bin/env python
# coding=utf-8

from time import sleep
from functools import wraps
import logging

points = [
    {'x': 1, 'y': 4}
    , {'x': 3, 'y': 2}
    , {'x': 2, 'y': 3}
    , {'x': 5, 'y': 5}
    , {'x': 4, 'y': 1}
]

print ('ori points', points)

points.sort()
print ('after sort', points)

points.sort(key=lambda item: item['y'], reverse=False)
print ('after sort', points)


listOne = [2, 3, 4]
listTwo = [2 * item for item in listOne if item > 2]
print ('listTow', listTwo)


assert len(listOne) >= 1

listOne.pop()
assert len(listOne) >= 1

listOne.pop()
assert len(listOne) >= 1

listOne.pop()
try:
    assert len(listOne) >= 1
except AssertionError as error:
    print ('error', error)



print ("\n\nretry装饰器 decorator\n")

logging.basicConfig()
log = logging.getLogger("retry")

def retry(function):
    @wraps(function)
    def wrapped_f(*args, **kwargs):
        MAX_ATTEMPTS = 5
        for attempt in range(1, MAX_ATTEMPTS + 1):
            try:
                print ('Before invoke original function')
                return function(*args, **kwargs)
            except:
                # log.exception("Attempt %s/%s failed : %s", attempt, MAX_ATTEMPTS, (args, kwargs))
                print ("Attempt {}/{} failed : {}\n".format(attempt, MAX_ATTEMPTS, (args, kwargs)))
                sleep(2 * attempt)
        # log.critical("All %s attempts failed : %s", MAX_ATTEMPTS, (args, kwargs))
        print ('ALl {} attempts failed : {}'.format(MAX_ATTEMPTS, (args, kwargs)))
    return wrapped_f



counter = 0

@retry
def saveToDatabase(arg):
    print ('Write to a database or make a network call or etc.')
    print ('This will be automatically retried if exception is thrown.')
    global counter
    counter += 1
    if counter < 2:
        raise ValueError(arg)

if __name__ == '__main__':
    saveToDatabase('Some bad value')



