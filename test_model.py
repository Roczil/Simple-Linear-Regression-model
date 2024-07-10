import unittest
import tensorflow as tf
from model import Model
from utilis import calculate_loss

class TestModel(unittest.TestCase):
    def test_initial_weights(self):
        model = Model()
        self.assertEqual(model.weight.numpy(), 10.0)
        self.assertEqual(model.bias.numpy(), 10.0)

    def test_calculate_loss(self):
        y_actual = tf.constant([1.0, 2.0, 3.0])
        y_output = tf.constant([1.0, 2.0, 3.0])
        loss = calculate_loss(y_actual, y_output)
        self.assertEqual(loss.numpy(), 0.0)

if __name__ == "__main__":
    unittest.main()
