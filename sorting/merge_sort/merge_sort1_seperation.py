# Separation

# What is sorted by a sort? A sort takes in a list of some data. The data can be words that we want to sort in dictionary order, or people we want to sort by birth date, or really anything else that has an order. For the simplicity of this lesson, we’re going to imagine the data as just numbers.
# The first step in a merge sort is to separate the data into smaller lists. Then we break those lists into even smaller lists. Then, when those lists are all single-element lists, something amazing happens! Well, kind of amazing. Well, you might have expected it, we do call it a “merge sort”. We merge the lists.

# Define a function called merge_sort(). Give merge_sort() one parameter: items.
def merge_sort(items):
  # We’re going to use merge_sort() to break down items into smaller and smaller lists, and then write a merge() function that will combine them back together.
  # For now, check the length of items. If items has length one or less, return items.
  if len(items) <= 1:
    return items