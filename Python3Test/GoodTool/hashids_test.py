#!/usr/bin/env python
# coding=utf-8

import hashids

hasher = hashids.Hashids(salt='kaiKaiTest', min_length=10)

e123456 = hasher.encode(123456)
e123456_2 = hasher.encode('123456')  # 非数字则是空

d123456 = hasher.decode(e123456)
d123456_2 = hasher.decode(e123456_2)  # 空tuple

print('e1=%s e2=%s d1=%s d2=%s' % (e123456, e123456_2, d123456, d123456_2))

e1_2_3_4 = hasher.encode(1, 2, 3, 4)
d1_2_3_4 = hasher.decode(e1_2_3_4)

print('e1_2_3_4=%s d1_2_3_4=%s  d0=%s' % (e1_2_3_4, d1_2_3_4, d1_2_3_4[0]))

# encode后都是str， decode后是tuple
