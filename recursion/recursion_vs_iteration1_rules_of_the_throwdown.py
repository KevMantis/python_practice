# Rules of the Throwdown

# This lesson will provide a series of algorithms and an iterative or recursive implementation.
# Anything we write iteratively, we can also write recursively, and vice versa. Often, the difference is substituting a loop for recursive calls.
# Your mission is to recreate the algorithm using the alternative strategy. If the example is recursive, write the algorithm using iteration. If the algorithm uses iteration, solve the problem using recursion.
# By the end of this lesson, you’ll have gained a better understanding of the different strategies to implement an algorithm, and along the way, we’ll discuss the big O runtimes of each algorithm.
# Each exercise will have a single checkpoint. You can implement the algorithm however you like as long as you’re following the prescribed approach (iterative or recursive).
# If you’re feeling stuck, the hint will give a detailed breakdown of how to implement the algorithm.
# We’ll start with a classic recursive example, factorial(). This function returns the product of every number from 1 to the given input.
"""
# runtime: Linear - O(N)
def factorial(n):  
  if n < 0:    
    ValueError("Inputs 0 or greater only") 
  if n <= 1:    
    return 1  
  return n * factorial(n - 1)

factorial(3)
# 6
factorial(4)
# 24
factorial(0)
# 1
factorial(-1)
# ValueError "Input must be 0 or greater"
"""
# This is a linear implementation, or O(N), where N is the number given as input.

# Implement your version of factorial() which has the same functionality without using any recursive calls!
def factorial(n):
  result = 1
  while n != 0:
    result *= n
    n -= 1
  return result

# test cases
print(factorial(3) == 6)
print(factorial(0) == 1)
print(factorial(5) == 120)