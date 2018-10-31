import tensorflow as tf
#import cv2
uu = 0
state = tf.Variable(0, name="counter")

one = tf.constant(1)
new_value = tf.add(state, one)
update = tf.assign(state, new_value)
init_op = tf.global_variables_initializer()
tf.summary.histogram("count",state)
with tf.Session() as sess:
    summary_waiter = tf.summary.FileWriter("C:\\tensor\log2",tf.get_default_graph())
    summary_log = tf.summary.merge_all()
    sess.run(init_op)
    for a in range(1000):
        _,summary=sess.run([update,summary_log])
        summary_waiter.add_summary(summary,a)
        if a % 50 == 0:
            print(a)


print('BBNNBB')
print('xxx')