#!/usr/bin/env python3
# coding=utf-8

import tensorflow as tf
import numpy as np

# with tf.device('/cpu:0'):
#
#     sess = tf.Session()
#
#     # a_gpu = tf.Variable(0, name="a_gup")
#     # sess = tf.Session(config=tf.ConfigProto(allow_soft_placement=True))
#
#     hello = tf.constant('Hello, TensorFlow!')
#     print(sess.run(hello))
#
#     a = tf.constant(10)
#     b = tf.constant(32)
#     print(sess.run(a + b))
#
#     c = tf.constant('haHa')
#     print(sess.run(c))
#
#     sess.close()


identity_matrix = tf.diag([1.0, 3.0, 1.0])
A = tf.truncated_normal([2, 3])
B = tf.fill([2, 3], 5.0)
C = tf.random_uniform([3, 2], maxval=100)
D = tf.convert_to_tensor(np.array([[1., 2., 3.], [-3., -7., -1.], [0., 5., -2.]]))
sess = tf.Session()
# sess.run(tf.global_variables_initializer())

print('\nI=')
print(sess.run(identity_matrix))
print('\nA=')
print(sess.run(A))
print('\nB=')
print(sess.run(B))
print('\nC=')
C = sess.run(C)
print(C)
print('\nD=')
print(sess.run(D))

print('\nA+B=')
print(sess.run(A+B))

print('\nB-B=')
print(sess.run(B-B))

print('\nB*I=')
BI = tf.matmul(B, identity_matrix)
print(sess.run(BI))

print('\ntranspose(C)=')
print(sess.run(tf.transpose(C)))

print('\ntranspose(D)=')
print(sess.run(tf.transpose(D)))

print('\ninverse(D)=')
print(sess.run(tf.matrix_inverse(D)))

print('\ndeterminant(D)={:.1f}'.format(sess.run(tf.matrix_determinant(D))))

print('\ncholesky(D):')
print(sess.run(tf.cholesky(identity_matrix)))

print('\nselfAdjointEig(D):')
print(sess.run(tf.self_adjoint_eig(D)))


sess.close()




