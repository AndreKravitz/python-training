def sum_one(x):
    return x + 1


def high_ord_func(x, func):
    return x + func(x)


result = high_ord_func(2, sum_one)
# result = 2 + (2 + 1)
print(result)


# HOF whit Lambda
def sum_three(x): return x + 3


def hof_lambda(x, func): return x + func(x)


result = hof_lambda(3, sum_three)
# result = 3 + (3 + 3)
print(result)

# HOF whit integrated Lambda
result = hof_lambda(5, lambda x: x * 5)
print(result)
# result = 5 + (5 * 5)
