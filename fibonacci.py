import math


# A utility function that will return true
# if the number is perfect square, else this
# will return false
def isPerfectSquare(num):
    # finding the square root of num
    s = int(math.sqrt(num))
    return s * s == num


def isFibonacciNumber(n):
    # return true if the number is fibonacci otherwise
    # return false
    return isPerfectSquare(5 * n * n + 4) or isPerfectSquare(5 * n * n - 4)


n = int(input("Enter the number you want to check : "))
if isFibonacciNumber(n):
    print(n, " Given number is fibonacci number")
else:
    print(n, " is not a fibonacci number")
