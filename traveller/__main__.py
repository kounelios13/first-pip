from .tourist import Tourist
import sys


def main():
    if len(sys.argv) > 1:
        name = sys.argv[1]
        t = Tourist(name)
        t.say_hello()
    else:
        print("Enter a tourist name next time")


if __name__ == '__main__':
    main()
