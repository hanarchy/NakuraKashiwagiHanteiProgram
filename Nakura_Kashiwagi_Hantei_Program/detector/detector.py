import tensorflow as tf
from .analysis_morphologic import create_datasets

ckpt_path = "Nakura_Kashiwagi_Hantei_Program/detector/wjn_model.ckpt"


class Detector():

    def __init__(self):
        # super().__init__()
        print('unko')
        # 学習済みモデルの構築
        dict_size = 180
        hidden1_size = 50
        hidden2_size = 10
        output_size = 2
        self.x = tf.placeholder(tf.float32, shape=[None, dict_size])

        with tf.name_scope("inference") as scope:
            W1 = tf.Variable(tf.zeros([dict_size, hidden1_size]),
                             name="weight_1")
            b1 = tf.Variable(tf.zeros([hidden1_size]),
                             name="bias_1")

            h1 = tf.nn.sigmoid(tf.matmul(self.x, W1) + b1)

            W2 = tf.Variable(tf.zeros([hidden1_size, hidden2_size]),
                             name="weight_2")
            b2 = tf.Variable(tf.zeros([hidden2_size]),
                             name="bias_2")

            h2 = tf.nn.sigmoid(tf.matmul(h1, W2) + b2)

            W3 = tf.Variable(tf.zeros([hidden2_size, output_size]),
                             name="weight_3")
            b3 = tf.Variable(tf.zeros([output_size]),
                             name="bias_3")

        self.y = tf.nn.softmax(tf.nn.relu(tf.matmul(h2, W3) + b3))
        saver = tf.train.Saver([W1, b1, W2, b2, W3, b3])
        self.sess = tf.Session()
        saver.restore(self.sess, ckpt_path)

    def detect_author(self, content):
        dict = create_datasets([content])
        result = self.sess.run(self.y, feed_dict={self.x: dict})
        return result
