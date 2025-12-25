import json
import matplotlib.pyplot as plt
from datetime import datetime

def save_image(data, filename):
    plt.imshow(data, cmap="inferno")
    plt.axis("off")
    plt.savefig(filename, dpi=300)
    plt.close()

def save_params(params):
    with open("params.json", "w", encoding="utf-8") as f:
        json.dump(params, f, indent=4, ensure_ascii=False)