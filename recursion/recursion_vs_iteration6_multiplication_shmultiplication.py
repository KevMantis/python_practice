# Multiplication? Schmultiplication!

# All programming languages you’re likely to use will include arithmetic operators like +, -, and *.
# Let’s pretend Python left out the multiplication, *, operator.
# How could we implement it ourselves? Well, multiplication is repeated addition. We can use a loop!
# Here’s an iterative approach:
"""
def multiplication(num_1, num_2):
  result = 0
  for count in range(0, num_2):
    result += num_1
  return result

multiplication(3, 7)
# 21
multiplication(5, 5)
# 25
multiplication(0, 4)
# 0
"""
# This implementation isn’t quite as robust as the built-in operator. It won’t work with negative numbers, for example. We don’t expect your implementation to handle negative numbers either!
# What is the big O runtime of our implementation?

# Implement your version of multiplication() which has the same functionality using recursive calls!
def multiplication(num_1, num_2):
  if num_1 == 0 or num_2 == 0:
    return 0
  return num_1 + multiplication(num_1, num_2 - 1)

# test cases
print(multiplication(3, 7) == 21)
print(multiplication(5, 5) == 25)
print(multiplication(0, 4) == 0)