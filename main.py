import sys


def usage(program_name):
    print("Usage: {} number1 operation number".format(program_name))
    print("Available operations:")
    print("\tadd")
    print("\tsub")
    print("\tmul")
    print()


def main():
    if len(sys.argv) == 4:
        number1 = int(sys.argv[1])
        operation = sys.argv[2]
        number2 = int(sys.argv[3])

        if operation == "add":
            result = number1 + number2
            print("{} + {} = {}".format(number1, number2, result))
            return

        if operation == "sub":
            result = number1 - number2
            print("{} - {} = {}".format(number1, number2, result))
            return

        if operation == "mul":
            result = number1 * number2
            print("{} * {} = {}".format(number1, number2, result))
            return

    usage(sys.argv[0])


if __name__ == "__main__":
    main()
