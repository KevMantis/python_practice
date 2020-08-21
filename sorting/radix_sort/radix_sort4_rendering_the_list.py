# Rendering the List

# For every iteration, radix sort renders a version of the input list that is sorted based on the digit that was just looked at. At first pass, only the ones digit is sorted. At the second pass, the tens and the ones are sorted. This goes on until the digits in the largest position of the largest number in the list are all sorted, and the list is sorted at that time.
# Here we’ll be rendering the list, at first, it will just return the list sorted so just the ones digit is sorted.

def radix_sort(to_be_sorted):
  maximum_value = max(to_be_sorted)
  max_exponent = len(str(maximum_value))

  being_sorted = to_be_sorted[:]
  digits = [[] for i in range(10)]

  for number in being_sorted:
    number_as_a_string = str(number)
    digit = number_as_a_string[-1]
    digit = int(digit)
    
    digits[digit].append(number)
  # Outside of our for loop which appends the numbers in our input list to the different buckets in digits, let’s render the list.
  # Since we know that all of our input numbers are in digits we can safely clear out being_sorted. We’ll make it an empty list and then add back in all the numbers from digits as they appear.
  # Assign an empty list to being_sorted.
  being_sorted = []
  # Now, create a for loop that iterates through each of our lists in digits.
  # Call each of these lists numeral because they each correspond to one specific numeral from 0 to 9.
  for numeral in digits:
    # Now use the .extend() method (which appends all the elements of a list, instead of appending the list itself) to add the elements of numeral to being_sorted.
    being_sorted.extend(numeral)
  # Unindent out of the for loop and return being_sorted.
  return being_sorted