import logging


logging.basicConfig(level=logging.INFO)


def main():
    total_sum = 0
    logging.info("Enter numbers to sum ('quit' or 'exit' to exit).")
    while True:
        input_text = input()
        if (input_text == "exit" or input_text == "quit"):
            break
        try:
            total_sum += int(input_text)
            logging.info("Sum: {0}".format(total_sum))
        except ValueError:
            logging.error("It's not a number!")


if __name__ == "__main__":
    main()

