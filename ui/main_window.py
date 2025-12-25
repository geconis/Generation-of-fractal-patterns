import tkinter as tk
from tkinter import ttk
from core.mandelbrot import generate_mandelbrot
from core.julia import generate_julia
from data.storage import save_image, save_params
from infra.logger import setup_logger
import logging

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

class MainWindow:
    def __init__(self):
        setup_logger()
        self.root = tk.Tk()
        self.root.title("Генератор фракталів")

        #Панель вибору фракталу
        tk.Label(self.root, text="Вибір фракталу:").pack()
        self.fractal_var = tk.StringVar(value="Mandelbrot")
        self.fractal_menu = ttk.OptionMenu(self.root, self.fractal_var, "Mandelbrot", "Mandelbrot", "Julia")
        self.fractal_menu.pack()

        #Кількість ітерацій
        tk.Label(self.root, text="Кількість ітерацій:").pack()
        self.iter_entry = tk.Entry(self.root)
        self.iter_entry.insert(0, "100")
        self.iter_entry.pack()

        #Кнопки
        tk.Button(self.root, text="Згенерувати", command=self.generate).pack()
        tk.Button(self.root, text="Zoom In", command=lambda: self.zoom(1.2)).pack()
        tk.Button(self.root, text="Zoom Out", command=lambda: self.zoom(0.8)).pack()

        #Місце для відображення фрактала
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas.get_tk_widget().pack()
        self.current_image = None
        self.zoom_factor = 1.0

    def generate(self):
        max_iter = int(self.iter_entry.get())
        fractal_type = self.fractal_var.get()
        logging.info(f"Генерація {fractal_type} з {max_iter} ітераціями")

        #Генерація даних
        if fractal_type == "Mandelbrot":
            data = generate_mandelbrot(800, 800, max_iter)
        elif fractal_type == "Julia":
            data = generate_julia(800, 800, max_iter)

        #Відображення у вікні
        self.ax.clear()
        self.ax.imshow(data, cmap='hot', extent=[-2, 2, -2, 2])
        self.ax.set_title(f"{fractal_type} fractal")
        self.canvas.draw()

        #Збереження даних
        save_image(data, f"{fractal_type.lower()}.png")
        save_params({"type": fractal_type, "iterations": max_iter})

        self.current_image = data
        self.zoom_factor = 1.0

    def zoom(self, factor):
        if self.current_image is None:
            return
        self.zoom_factor *= factor
        size_x, size_y = self.current_image.shape
        center_x, center_y = size_x // 2, size_y // 2
        new_size_x, new_size_y = int(size_x / self.zoom_factor), int(size_y / self.zoom_factor)

        start_x = max(center_x - new_size_x // 2, 0)
        end_x = min(center_x + new_size_x // 2, size_x)
        start_y = max(center_y - new_size_y // 2, 0)
        end_y = min(center_y + new_size_y // 2, size_y)

        zoomed = self.current_image[start_y:end_y, start_x:end_x]
        self.ax.clear()
        self.ax.imshow(zoomed, cmap='hot', extent=[-2, 2, -2, 2])
        self.ax.set_title(f"Zoom x{self.zoom_factor:.2f}")
        self.canvas.draw()

    def run(self):
        self.root.mainloop()