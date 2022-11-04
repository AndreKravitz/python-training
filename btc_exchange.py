# Currency exchange to Bitcoin

def conversor(currency_value, valor_btc):
    currency = input("How many " + currency_value + " do you have?: ")
    currency = float(currency)
    bitcoin = currency * valor_btc
    bitcoin = str(bitcoin)
    print("You have BTC " + bitcoin)


menu = '''
Welcome to the Bitcoin exchange currency calculator

1- USD
2- EUR
3- CNY

Press 1, 2, or 3 to select your currency: '''

option = int(input(menu))

if option == 1:
    conversor("Dollars", 0.0000426)
elif option == 2:
    conversor("Euros", 0.0000422)
elif option == 3:
    conversor("Chinese Yuan", 0.0000058)
else:
    print("ERROR: Unknown option")
