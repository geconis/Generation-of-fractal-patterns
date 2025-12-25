import numpy as np

def generate_julia(width, height, max_iter, c=-0.7+0.27015j):
    x = np.linspace(-1.5, 1.5, width)
    y = np.linspace(-1.5, 1.5, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    img = np.zeros(Z.shape, dtype=int)

    for i in range(max_iter):
        mask = np.abs(Z) < 2.0
        img[mask] = i
        Z[mask] = Z[mask]**2 + c

    return img