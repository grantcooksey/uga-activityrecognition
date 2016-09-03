from parser import Parser
import sys


def main():
    Parser.parse_file(sys.argv[1])

if __name__ == "__main__":
    main()
