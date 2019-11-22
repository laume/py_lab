from src.a.file_a import func_a
from src.file_b import func_b

def func_test():
    return f'func_test name {__name__}, and a: {func_a()} and b: {func_b()}'


print(func_test())