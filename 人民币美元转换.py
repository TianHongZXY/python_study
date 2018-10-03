money = input()
if money[0] in ['R','r']:
    USD = (eval(money[3:]) )/6.78
    print("USD{:.2f}".format(USD))
elif money[0] in ['U','u']:
    RMB = 6.78*eval(money[3:])
    print("RMB{:.2f}".format(RMB))
