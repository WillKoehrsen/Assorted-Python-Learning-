import tensorflow as tf 

# computation graph
x1 = tf.constant(8)
x2 = tf.constant(11)

result = tf.multiply(x1 , x2)

# automatically closes the session, can also be used with files to automatically close
with tf.Session() as sess:
	output = sess.run(result)
	#print(putput)

print(output)




