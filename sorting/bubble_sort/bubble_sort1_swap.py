# Bubble Sort: Swap

# The Bubble Sort algorithm works by comparing a pair of neighbor elements and shifting the larger of the two to the right. Bubble Sort completes this by swapping the two elements’ positions if the first element being compared is larger than the second element being compared.
# Below is a quick pseudocode example of what we will create:
"""
for each pair(elem1, elem2):
  if elem1 > elem2:
    swap(elem1, elem2)
  else:
    # analyze next set of pairs
"""
# This swap() sub-routine is an essential part of the algorithm. Bubble sort swaps elements repeatedly until the largest element in the list is placed at the greatest index. This looping continues until the list is sorted.
# This GIF illustrates how swap() method works. https://s3.amazonaws.com/codecademy-content/courses/sorting/swap.gif

nums = [5, 2, 9, 1, 5, 6]

# Define the function swap() which has three parameters: arr, index_1, and index_2.
# Write pass in the body of the function for now.
def swap(arr, index_1, index_2):
  # Inside swap(), remove pass.
  # Create the variable temp and assign to it the value located at index_1 of arr.
  #pass
  temp = arr[index_1]
  # After declaring temp, set the value at index_1 of arr to be the value at index_2 of arr.
  # Then, set the value located at index_2 to be temp.
  arr[index_1] = arr[index_2]
  arr[index_2] = temp

# Uncomment the code at the bottom of the file to test out swap().
swap(nums, 3, 5)
print(nums)