import random
number = random.randint(-10, 10)
if number > 0:
    print("%d is positive\n"%(number));
elif number < 0:
    print("%d is negative\n"%(number));
else:
    print("%d is zero\n"%(number));