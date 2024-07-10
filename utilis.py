import tensorflow as tf
import numpy as np

def calculate_loss(y_actual, y_output):
    return tf.reduce_mean(tf.square(y_actual - y_output))

def train(model, x, y, learning_rate):
    with tf.GradientTape() as gt:
        y_output = model(x)
        loss = calculate_loss(y, y_output)
    
    new_weight, new_bias = gt.gradient(loss, [model.weight, model.bias])
    model.weight.assign_sub(new_weight * learning_rate)
    model.bias.assign_sub(new_bias * learning_rate)

def generate_data(m, b, num_points=100):
    x = np.linspace(0, 4, num_points)
    # Użycie listy składanej do generowania y
    y = np.array([m * xi + b + np.random.randn() * 0.25 for xi in x])
    return x, y

def plot_data(x, y, model=None):
    import matplotlib.pyplot as plt
    plt.scatter(x, y)
    if model:
        new_x = np.linspace(0, 4, 50)
        new_y = model.weight.numpy() * new_x + model.bias.numpy()
        plt.plot(new_x, new_y, color='red')
    plt.show()
