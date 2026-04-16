import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        # He initialization for hidden layer
        self.weights1 = np.random.randn(input_size, hidden_size) * np.sqrt(2. / input_size)
        self.bias1 = np.zeros((1, hidden_size))
        # Xavier initialization for output layer
        self.weights2 = np.random.randn(hidden_size, output_size) * np.sqrt(1. / hidden_size)
        self.bias2 = np.zeros((1, output_size))

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-np.clip(x, -500, 500)))

    def sigmoid_derivative(self, x):
        # x is the sigmoid output
        return x * (1 - x)

    def relu(self, x):
        return np.maximum(0, x)

    def relu_derivative(self, x):
        return (x > 0).astype(float)

    def forward(self, X):
        self.layer1_input = np.dot(X, self.weights1) + self.bias1
        self.layer1_output = self.sigmoid(self.layer1_input) # Changed back to sigmoid for XOR simplicity
        self.layer2_input = np.dot(self.layer1_output, self.weights2) + self.bias2
        self.output = self.sigmoid(self.layer2_input)
        return self.output

    def backward(self, X, y, output, learning_rate):
        m = y.shape[0]

        # Error at output layer (Cross-entropy with sigmoid)
        error_output = output - y

        d_weights2 = np.dot(self.layer1_output.T, error_output) / m
        d_bias2 = np.sum(error_output, axis=0, keepdims=True) / m

        # Error at hidden layer
        error_hidden = np.dot(error_output, self.weights2.T) * self.sigmoid_derivative(self.layer1_output)

        d_weights1 = np.dot(X.T, error_hidden) / m
        d_bias1 = np.sum(error_hidden, axis=0, keepdims=True) / m

        # Update weights and biases
        self.weights1 -= d_weights1 * learning_rate
        self.bias1 -= d_bias1 * learning_rate
        self.weights2 -= d_weights2 * learning_rate
        self.bias2 -= d_bias2 * learning_rate

    def train(self, X, y, epochs=1000, learning_rate=0.1):
        for epoch in range(epochs):
            output = self.forward(X)
            self.backward(X, y, output, learning_rate)
            if epoch % 1000 == 0:
                # Binary Cross-Entropy Loss
                loss = -np.mean(y * np.log(output + 1e-15) + (1 - y) * np.log(1 - output + 1e-15))
                print(f"Epoch {epoch}, Loss: {loss:.4f}")

    def predict(self, X):
        return self.forward(X)
