'''
print(0 / 0) 
print(result)
# ERROR (Program stops)
print('I appeared because the ERROR has failed')
'''


def suma(x, y):
    return x + y  # Modify to cause ERROR


try:
    print(0 / 0)  # ERROR 1
    assert 1 != 1, 'One is not equal to one'  # ERROR 2
    assert suma(2, 2) == 4  # ERROR 3
    age = 10
    if age < 18:
        raise Exception('Access denied')  # ERROR 4

except ZeroDivisionError as error:
    print(error)
except AssertionError as error:
    print(error)
except Exception as error:
    print(error)

print('Still working!')
