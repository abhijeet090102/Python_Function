def apply_t(fun,arg):
    return fun(fun(arg))
def add_five(x):
    return x*x
print(apply_t(add_five,2))
