try:
    from a.file_a import func_a
except:
    from .a.file_a import func_a



def func_b():
    return f'2: file_b func_b  name: {__name__}, and imported a: {func_a()}'
