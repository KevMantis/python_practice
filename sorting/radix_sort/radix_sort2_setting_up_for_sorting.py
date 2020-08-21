# Setting Up For Sorting

# In this implementation, we’re going to build the radix sort naturally, from the inside out. The first step we’re going to take is going to be our inner-most loop, so that we know we’ll be solid when we’re iterating through each of the exponents.

def radix_sort(to_be_sorted):
  maximum_value = max(to_be_sorted)
  max_exponent = len(str(maximum_value))
  # By the nature of a radix sort we need to erase and rewrite our output list a number of times. It would be bad practice to mutate the input list — in case something goes wrong with our code, or someone using our sort decides they don’t want to wait anymore. We wouldn’t want anyone out there to have to deal with the surprise of having their precious list of integers mangled.
  # Create a copy of to_be_sorted and save the copy into a new list called being_sorted.
  being_sorted = to_be_sorted[:]
  # A radix sort goes through each position of each number and puts all of the inputs in different buckets depending on the value . Since there are 10 different values (that is, 0 through 9) that a position can have, we need to create ten different buckets to put each number in.
  # Create a list of ten empty lists and assign the result to a variable called digits. Then return digits.
  digits = [[] for digit in range(10)]
  return digits