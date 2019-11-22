from file_b import func_b

def func_c():
    return f'3: file_c func_c name: {__name__}, and b: {func_b()}'

print(func_c())