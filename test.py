import unittest
import numpy as np
from core.mandelbrot import generate_mandelbrot
from core.julia import generate_julia

class TestFractals(unittest.TestCase):
    def test_mandelbrot_basic(self):
        """Перевірка базової генерації Мандельброта"""
        width, height = 100, 100
        max_iter = 50
        result = generate_mandelbrot(width, height, max_iter)
        self.assertIsInstance(result, np.ndarray)
        self.assertEqual(result.shape, (height, width))
        self.assertTrue(np.max(result) <= max_iter)

    def test_julia_basic(self):
        """Перевірка базової генерації Джулії"""
        width, height = 100, 100
        max_iter = 50
        c = complex(-0.7, 0.27015)
        result = generate_julia(width, height, max_iter, c)
        self.assertIsInstance(result, np.ndarray)
        self.assertEqual(result.shape, (height, width))
        self.assertTrue(np.max(result) <= max_iter)

if __name__ == "__main__":
    unittest.main()
