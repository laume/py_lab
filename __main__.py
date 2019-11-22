import sys

from src import file_b
from src import file_c
from src.options import file_a


def run_project(args):
    print(file_a.func_a())
    print(file_b.func_b())
    print(file_c.func_c())


if __name__ == '__main__':
    run_project(sys.argv)
