#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
print("Last digit of %d is %d"%(number, last_digit))
if last_digit > 5:
    print("and is greater than 5\n")
elif last_digit == 0:
    print("and is 0\n")
elif last_digit < 6 and last_digit != 0:
    print("and is less than 6 and not 0\n")
