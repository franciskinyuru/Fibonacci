# Check If a Number is Fibonacci

# Functional implementation of the approach: 
A utility function that will return true
if the number is perfect square, else this
will return false
def isPerfectSquare(num):
# finding the square root of num
s =int(math.sqrt(num))
return s*s == num
def isFibonacciNumber(n):
# return true if the number is fibonacci otherwise
# return false
return isPerfectSquare(5nn + 4) or isPerfectSquare(5nn – 4)
