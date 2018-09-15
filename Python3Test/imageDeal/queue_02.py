#!/usr/bin/env python3
# coding=utf-8

import tensorflow as tf
import numpy as np
import threading
import time


def my_loop(coord, worker_id):
    while not coord.should_stop():
        if np.random.rand() < 0.05:
            print(f'Stop from id: {worker_id}')
            coord.request_stop()
        else:
            print(f'Working on id: {worker_id}')
        time.sleep(1)


coord = tf.train.Coordinator()
threads = [threading.Thread(target=my_loop, args=(coord, i)) for i in range(5)]
for t in threads:
    t.start()
coord.join(threads)
print('all thread finished')
