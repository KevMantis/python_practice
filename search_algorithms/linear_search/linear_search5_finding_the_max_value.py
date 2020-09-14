# Finding the Maximum Value

# The largest value of a sorted list conveniently is the last element of a list. The largest value of an unsorted list, however, is not guaranteed to be the last element.
# Imagine that you are a teacher who wants to know the highest score your students scored on a test. Consider the following unsorted list of test scores:
"""
test_scores = [88, 93, 75, 100, 80, 67, 71, 92, 90, 83]
"""
# 100 is the highest score in the list, but it is the 4th element of the list.
# In order to find the highest score, we must sequentially scan the entire list for the largest value and keep track of the largest value that we have seen to date. Using test_scores, we would keep track of the high score as follows:
# - In the first iteration, 88 is the highest test score.
# - In the second iteration, 93 is the highest score because it is greater than 88.
# - In the third iteration, 93 is the highest score because it is greater than 75.
# - In the fourth iteration, 100 is the highest score because it is greater than 93.
# This continues until you reach the end of the list.
# In order to find the largest value in a list, we modify the algorithm to match the following pseudocode:
"""
# Create a variable called max_value_index    
# Set max_value_index to the index of the first element of the search list
     # For each element in the search list
          # if element is greater than the element at max_value_index
               # Set max_value_index equal to the index of the element
# return max_value_index
"""
# Let’s implement this in Python.

# Search list
test_scores = [88, 93, 75, 100, 80, 67, 71, 92, 90, 83]

#Linear Search Algorithm
#def linear_search(search_list, target_value):
# We do not need to provide a target value to the function because we’re looking for the largest value.
# Change the function declaration of linear_search() to one parameter, search_list.
def linear_search(search_list):
  # On the first line within linear_search(), create a variable maximum_score_index with a value of None.
  # This will track the highest value visited during the search.
  maximum_score_index = None
  for idx in range(len(search_list)):
    print(search_list[idx])
    #if search_list[idx] == target_value:
    #  return idx
  #raise ValueError("{0} not in list".format(target_value))
    # As we iterate through the list, we want to check whether each element is greater than the element at maximum_score_index.
    # Change the condition of the if statement:
    # - if maximum_score_index is None
    # - OR
    # - if the element of search_list is greater than the element at the maximum_score_index of search_list.
    # In either of the two conditions:
    # - update maximum_score_index to the index of the current element.
    # Currently, the linear search function raises a ValueError after iterating through the list.
    # Remove that line and return maximum_score_index
    if maximum_score_index == None or search_list[idx] > search_list[maximum_score_index]:
      maximum_score_index = idx
  return maximum_score_index

# Function call
highest_score = linear_search(test_scores)

#Prints out the highest score in the list
print(highest_score)