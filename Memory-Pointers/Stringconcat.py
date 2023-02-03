from timeit import timeit

def add(items):
    result = ""
    for item in items:
        result+=item
    return result
# add takes longer time than join
huge_list = ["hi"] * 30
print(timeit('add(huge_list)', 'from __main__ import add, huge_list'))
print(timeit('"".join(huge_list)', 'from __main__ import add, huge_list'))
