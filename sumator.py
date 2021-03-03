#!/usr/bin/env python3
"""Sumator

This script contains a single function that continually
reads numbers from STDIN and sums them up.
"""

import logging


logging.basicConfig(level=logging.INFO, format="%(message)s")


def main():
    """ Main function containing infinite loop """

    total_sum = 0

    logging.info("Enter numbers to sum ('quit' or 'exit' to exit).")
    while True:
        input_text = input()

        if input_text in ("exit", "quit"):
            break

        try:
            total_sum += int(input_text)
        except ValueError:
            logging.error("It's not a number!")
        else:
            logging.info("Sum: %d", total_sum)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
