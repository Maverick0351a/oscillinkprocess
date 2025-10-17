import logging
import os
import sys


def init_logging(run_dir: str, name: str = "oscillink", level: int = logging.INFO) -> logging.Logger:
    os.makedirs(run_dir, exist_ok=True)
    log_file = os.path.join(run_dir, f"{name}.log")

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.handlers.clear()

    fh = logging.FileHandler(log_file, encoding="utf-8")
    fh.setLevel(level)
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(level)

    fmt = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
    fh.setFormatter(fmt)
    ch.setFormatter(fmt)

    logger.addHandler(fh)
    logger.addHandler(ch)
    logger.propagate = False
    return logger
