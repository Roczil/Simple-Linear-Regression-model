import tensorflow as tf

class Model:
    def __init__(self):
        self.weight = tf.Variable(10.0)
        self.bias = tf.Variable(10.0)
    
    def __call__(self, x):
        return self.weight * x + self.bias
