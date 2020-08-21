# Bucketing Numbers

# The least significant digit radix sort algorithm takes each number in the input list, looks at the digits of that number in order from right to left, and incrementally stuffs each number into the bucket corresponding to the value of that digit.
# First we’re going to write this logic for the least significant digit, then we’re going to loop over the code we write to do that for every digit.

def radix_sort(to_be_sorted):
  maximum_value = max(to_be_sorted)
  max_exponent = len(str(maximum_value))

  being_sorted = to_be_sorted[:]
  digits = [[] for i in range(10)]
  # We’ll need to iterate over being_sorted. Grab each value of being_sorted and save it as the temporary variable number.
  for number in being_sorted:
    # Now convert number to a string and save that as number_as_a_string.
    number_as_a_string = str(number)
    # How do we get the last element of a string? This would correspond to the least significant digit of the number. For strings, this is simple, we can use a negative index.
    # Save the last element of number_as_a_string to the variable digit.
    digit = number_as_a_string[-1]
    # Now that we have a string containing the least significant digit of number saved to the variable digit. We want to use digit as a list index for digits. Unfortunately, it needs to be an integer to do that. But that should be easy for us to do:
    # Set digit equal to the integer form of digit.
    digit = int(digit)
    # We know that digits[digit] is an empty list (because digits has ten lists and digit is a number from 0 to 9). So let’s add our number to that list!
    # Call .append() on digits[digit] with the argument number.
    digits[digit].append(number)
  # Now break out of the for loop and return digits.
  return digits