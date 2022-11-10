#  Lambda function is a small anonymous function that takes one argument or more, but can only have one expression, and returns a result.

#  Lambda whit singel argument
x = lambda a : a + 10
print(x(5))


# Lambda whit multiple arguments
y = lambda a, b, c : a * b * c
print(y(10, 2, 3))    



# Lambda as a hidden function
def my_function(n):
    return lambda a : a * n


times_3 = my_function(3)
times_5 = my_function(5)


print(times_3(11))
print(times_5(100))