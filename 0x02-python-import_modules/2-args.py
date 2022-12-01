#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    count = len(sys.argv)

    if count == 1:
        print("0 arguments.")
        exit()
    elif count == 2:
        print("{:d} argument:".format(count - 1))
    else:
        print("{:d} arguments:".format(count - 1))

    for i in range(1, count):
        print("{:d}: {:s}".format((i), sys.argv[i]))
