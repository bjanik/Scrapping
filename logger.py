import logging

def logger(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Entering function {func.__name__}")
        res = func(*args)
        logging.info(f"Leaving function {func.__name__}")
        return res
    return wrapper