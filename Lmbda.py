# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

# Add 10 to argument a, and return the result:
x = lambda a : a + 10
print(x(5))

# Multiply argument a with argument b and return the result:
x = lambda a, b : a * b
print(x(5, 6))

# using in anoynomous functions
def myfunc(n):
      return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))