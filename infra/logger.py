import logging

def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        filename="app.log",
        filemode="a",
        encoding="utf-8"
    )