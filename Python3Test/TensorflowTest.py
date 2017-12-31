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

# print(sess.run(tf.random_normal(mean=10, shape=[10])))

# A = tf.Variable(tf.random_normal(shape=[1, 1]))
# sess.run(tf.global_variables_initializer())
# print(sess.run(A))

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
print(sess.run(A + B))

print('\nB-B=')
print(sess.run(B - B))

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

print(sess.run(tf.div(13, 4)))
print(sess.run(tf.truediv(13, 4)))
print(sess.run(tf.floordiv(13, 4)))
print(sess.run(tf.mod(13.2, 4)))

print(sess.run(tf.cross([1, 0, 0], [0, 1, 0])))
print(sess.run(tf.square([1, 2, 3])))


def custom_polynomial(local_tf, value):
    return local_tf.subtract(3 * local_tf.square(value), value) + 10


print((sess.run(custom_polynomial(tf, 11))))

sess.close()

print(13 / 4)
