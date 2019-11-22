from . import file_b


def func_c():
    return f'3: file_c func_c name: {__name__}, and b: {file_b.func_b()}'
