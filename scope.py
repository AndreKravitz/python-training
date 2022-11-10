# Local scope
def my_function():
    x = 300
    print(x)
    
my_function()    
x = 0

# Global scope
y = 500 
def my_function_2():
    print(y)
    
my_function_2()
print(y)


# Global Keyboard
def my_function_3():
    global z
    z = 700

my_function_3()
print(z)    