#!/usr/bin/env python3
# coding=utf-8

import tensorflow as tf

import numpy as np

tx = np.random.ranf(20)

ty = tx * 5 + 5

x = tf.placeholder("float", name='input')

y = tf.placeholder("float", name='output')

k = tf.Variable(6., name='k')

b = tf.Variable(0., name='b')

y_pred = tf.multiply(x, k)
y_pred = tf.add(y_pred, b, name='y_pred')
# y_pred = tf.add(k * x, b, name='y_pred')

loss = tf.square(y - y_pred)
loss = tf.reduce_sum(loss)

train = tf.train.GradientDescentOptimizer(0.03).minimize(loss)

min_loss = tf.constant(1e-3)

session = tf.Session()

session.run(tf.global_variables_initializer())

for i in range(500):
    session.run(train, feed_dict={x: tx, y: ty})
    # k_value, b_value, loss_value, is_ok = session.run([k, b, loss, loss < min_loss], feed_dict={x: tx, y: ty})
    # print('step=%s k=%s b=%s loss=%s' % (i, k_value, b_value, loss_value))
    # if is_ok:
    #     break
    k_value, b_value, loss_value = session.run([k, b, loss], feed_dict={x: tx, y: ty})
    print('step=%s k=%s b=%s loss=%s' % (i, k_value, b_value, str(loss_value)))

result = session.run([k, b])

print('tx=%s ty=%s result=%s' % (tx, ty, result))

output_graph_def = tf.graph_util.convert_variables_to_constants(session, session.graph_def,
                                                                output_node_names=['input', 'output', 'k', 'b',
                                                                                   'y_pred'])

f = tf.gfile.FastGFile('../logs/kai_line_mul_android.pb', mode='wb')

f.write(output_graph_def.SerializeToString())

f.close()

session.close()
