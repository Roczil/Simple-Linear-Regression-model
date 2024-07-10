import tensorflow as tf
import numpy as np
from model import Model
from utilis import train, generate_data, plot_data

def main():
    try:
        m = 2
        b = 0.5
        epochs = 100
        learning_rate = 0.15

        x, y = generate_data(m, b)
        model = Model()

        for epoch in range(epochs):
            y_output = model(x)
            loss = tf.reduce_mean(tf.square(y - y_output))
            if epoch % 10 == 0:
                print(f"Epoch: {epoch}, loss: {loss.numpy()}")
            train(model, x, y, learning_rate)

        print(f"Trained weight: {model.weight.numpy()}")
        print(f"Trained bias: {model.bias.numpy()}")

        plot_data(x, y, model)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
