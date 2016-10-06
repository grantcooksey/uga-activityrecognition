from parser import Parser
import sys


def main():
    if not len(sys.argv) == 2:
        print('Usage: single_file_driver.py <path_to_file>')
        sys.exit(1)
    Parser.parse_file(sys.argv[1])

if __name__ == "__main__":
    main()
