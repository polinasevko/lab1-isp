from math import sqrt

import logging


logging.basicConfig(level=logging.INFO)


def is_prime(num):
    if num < 2:
        return False

    if num == 2:
        return True

    limit = sqrt(num)
    ind = 2

    while ind <= limit:
        if num % ind == 0:
            return False
        ind += 1
    return True


def main():
    while True:
        try:
            num = int(input("is your number prime?"))
            break
        except ValueError:
            logging.info("Error: invalid input. Try more.")

    logging.info(is_prime(num))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.info("Error.")
