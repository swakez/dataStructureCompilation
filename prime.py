import math


def is_prime(n: int):
    if n == 1:
        return "{0} is not a prime number".format(num)
    for i in range(2, n):
        if n % i == 0:
            return "{0} is not a prime number".format(num)
    return "{0} is a prime number".format(num)


def is_prime_improved(n: int):
    if n == 1:
        return "{0} is not a prime number".format(num)
    for i in range(2, math.sqrt(n)):
        if n % i == 0:
            return "{0} is not a prime number".format(num)
    return "{0} is a prime number".format(num)


if __name__ == '__main__':
    num = input("Enter a number : ")
    num = int(num)
    print(is_prime(num))