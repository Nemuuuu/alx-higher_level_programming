def print_last_digit(number):
    if number < 0:
        return -1 * (number % 10)
    else:
        return number % 10
print(print_last_digit(98))
print(print_last_digit(0))
print(print_last_digit(-1024))