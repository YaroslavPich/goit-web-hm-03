""" Implementation of the paralel version """

import logging
from multiprocessing import Pool, cpu_count
from time import time

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)


def factorize(num):
    dividers = []
    for i in range(1, num + 1):
        if num % i == 0:
            dividers.append(i)
    return dividers


if __name__ == "__main__":
    numbers = [128, 255, 99999, 10651060]
    logging.info(f"Count CPU - {cpu_count()}")
    time_start = time()
    with Pool(cpu_count()) as pool:
        result = pool.map(factorize, numbers)
        pool.close()
    logging.info(f"{time() - time_start}")
    a, b, c, d = result
    logging.info(a)
    logging.info(b)
    logging.info(c)
    logging.info(d)
