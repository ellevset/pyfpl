
import sys
from pyfpl.core.management import run_from_cmd_line


def main(argv):
    run_from_cmd_line(argv)


if __name__ == '__main__':
    main(sys.argv[1:])