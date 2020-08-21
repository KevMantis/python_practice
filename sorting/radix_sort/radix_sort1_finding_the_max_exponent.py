# Finding the Max Exponent

# In our version of least significant digit radix sort, we’re going to utilize the string representation of each integer. This, combined with negative indexing, will allow us to count each digit in a number from right-to-left.
# Some other implementations utilize integer division and modular arithmetic to find each digit in a radix sort, but our goal here is to build an intuition for how the sort works.
# Our first step is going to be finding the max_exponent, which is the number of digits long the largest number is. We’re going to find the largest number, cast it to a string, and take the length of that string.

# Define your function radix_sort() that takes a list as input and call that input to_be_sorted.
def radix_sort(to_be_sorted):
  # In order to determine how many digits are in the longest number in the list, we’ll need to find the longest number.
  # Declare a new variable maximum_value and assign the max() of to_be_sorted to it.
  maximum_value = max(to_be_sorted)
  # Now we want to define our max_exponent.
  # - First, cast maximum_value to a string.
  # - Then take the len() of that string.
  # - Then assign that len() to a variable called max_exponent.
  # - Then return max_exponent.
  max_exponent = len(str(maximum_value))
  return max_exponent