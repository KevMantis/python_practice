# Bubble Sort: Compare

# Now that we know how to swap items in an array, we need to set up the loops which check whether a swap is necessary.
# Recall that Bubble Sort compares neighboring items and if they are out of order, they are swapped.
# What does it mean to be “out of order”? Since bubble sort is a comparison sort, we’ll use a comparison operator: <.
# We’ll have two loops:
# One loop will iterate through each element in the list.
# Within the first loop, we’ll have another loop for each element in the list.
# Inside the second loop, we’ll take the index of the loop and compare the element at that index with the element at the next index. If they’re out of order, we’ll make a swap!

nums = [5, 2, 9, 1, 5, 6]

def swap(arr, index_1, index_2):
  temp = arr[index_1]
  arr[index_1] = arr[index_2]
  arr[index_2] = temp
  
# Below the body of swap(), define a new function: bubble_sort() which has the parameter arr.
# Write pass in the body of bubble_sort to start.
def bubble_sort(arr):
  #pass
  # Inside bubble_sort(), replace pass with a for loop that iterates up until the last element of the list.
  # Inside the for loop, check if the value in arr at index is > the value in arr at index + 1.
  # If it is, use swap() and pass arr, index, and index + 1 as arguments.
  for e in arr:
    for i in range(len(arr) - 1):
      if arr[i] > arr[i + 1]:
        swap(arr, i, i + 1)
  # As you can see by the output, our list is not sorted!
  # One loop through the list is only sufficient to move the largest value to its correct placement.
  # Create another loop which iterates for each element in arr.
  # Move the entire contents of the function within this loop:
  """
  def bubble_sort(arr):
    for el in arr:
      # previous code goes here!
  """
  # Run the code again, your list should be sorted!

##### test statements

print("Pre-Sort: {0}".format(nums))      
bubble_sort(nums)
print("Post-Sort: {0}".format(nums))