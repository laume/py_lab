from . import options


def func_b():
    return f'2: file_b func_b  name: {__name__}, and imported a: {options.file_a.func_a()}'
