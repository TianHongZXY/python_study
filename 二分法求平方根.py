x = float(input())
import math
low = 0
high = x
guess =(low + high)/2

while abs(guess**2 - x)>1e-4:
    if guess**2 >x:
        high = guess
    else :
        low = guess
    guess =(low + high)/2
print(guess)
