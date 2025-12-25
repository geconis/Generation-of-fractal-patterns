import numpy as np

def generate_mandelbrot(width, height, max_iter):
    x = np.linspace(-2.5, 1.5, width)
    y = np.linspace(-2.0, 2.0, height)
    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y
    Z = np.zeros_like(C)
    output = np.zeros(C.shape)

    for i in range(max_iter):
        mask = np.abs(Z) <= 2
        Z[mask] = Z[mask] ** 2 + C[mask]
        output[mask] = i

    return output