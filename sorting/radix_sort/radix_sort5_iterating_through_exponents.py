# Iterating through Exponents

# We have the interior of our radix sort, which right now goes through a list and sorts it by the first digit in each number. That’s a pretty great start actually. It won’t be hard for us to go over every digit in a number now that we can already sort by a given digit.

def radix_sort(to_be_sorted):
  maximum_value = max(to_be_sorted)
  max_exponent = len(str(maximum_value))
  being_sorted = to_be_sorted[:]

  # After defining being_sorted for the first time in the function (and before defining digits which we’ll need per iteration), create a new for loop that iterates through the range() of max_exponent.
  # Use the variable name exponent as a temporary variable in your for loop, it will count the current exponent we’re looking at for each number.
  for exponent in range(max_exponent):
    # Now indent the rest of your function after this new for loop.
    # (Tip: You can highlight the text in your code editor and use the Tab key to increase the indentation of code.)

    # In our for loop we’re going to want to create the index we’ll use to get the appropriate position in the numbers we’re sorting.
    # First we’re going to create the position variable, which keeps track of what exponent we’re looking at. Since exponent is zero-indexed our position is always going to be one more than the exponent. Assign to it the value of exponent + 1.
    position = exponent + 1
    # Now we want to create our index that we’ll be using to index into each number! This index is going to be roughly the same as position, but since we’re going to be indexing the string in reverse it needs to be negative!
    # Set index equal to -position.
    index = -position

    digits = [[] for i in range(10)]

    for number in being_sorted:
      number_as_a_string = str(number)
      # Now in the body of our loop, let’s update our digit lookup to get the digit at the given index. Where we before used number_as_a_string[-1] we’ll want to start accessing [index] instead.
      # Update the line of code where we first define digit to access index in number_as_a_string.
      #digit = number_as_a_string[-1]
      digit = number_as_a_string[index]
      digit = int(digit)
      
      digits[digit].append(number)

    being_sorted = []
    for numeral in digits:
      being_sorted.extend(numeral)

  # Now we’ve got a sort going! At the very end of our function, de-indenting out of all the for loops (but not the function itself), return being_sorted. It will be sorted by this point!
  return being_sorted