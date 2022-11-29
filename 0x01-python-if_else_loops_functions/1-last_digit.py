#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    neg_num = number * -1
    last = (neg_num % 10) * -1
else:
    last = number % 10
if last > 5:
    print(f"Last digit of {number:d} is {last} and is greater than 5")
elif 6 > last != 0:
    print(f"Last digit of {number:d} is {last} and is less than 6 and not 0")
else:
    print(f"Last digit of {number:d} is {last} and is 0")
