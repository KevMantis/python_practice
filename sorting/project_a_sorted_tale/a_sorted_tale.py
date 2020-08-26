# A Sorted Tale

# You recently began employment at “A Sorted Tale”, an independent bookshop. Every morning, the owner decides to sort the books in a new way.
# Some of his favorite methods include:
# - By author name
# - By title
# - By number of characters in the title
# - By the reverse of the author’s name
# Throughout the day, patrons of the bookshop remove books from the shelf. Given the strange ordering of the store, they do not always get the books placed back in exactly the correct location.
# The owner wants you to research methods of fixing the book ordering throughout the day and sorting the books in the morning. It is currently taking too long!

import utils
import sorts

bookshelf = utils.load_books('books_small.csv')

# The owner provides the current state of the bookshelf in a comma-separated values, or csv, file. To get you started, we have provided a function load_books, defined in utils.py.
# Within script.py, we are loading the books from books_small.csv. This list of 10 books makes it easier to determine how the algorithms are behaving. we’ll use this to develop the algorithms and then we’ll try them out later on the larger file.
# Add a for loop to print the titles within the bookshelf.
# Save your code and run it using python3 script.py in the terminal.
for book in bookshelf:
  print(book['title'])

# Today’s sorting is by title and looking at the bookshelf it’s pretty close. Some patrons have placed books back in slightly the wrong place.
# Before we start solving the problem, we need to do a bit of data manipulation to ensure that we compare books correctly. Python’s built-in comparison operators compare letters lexicographically based on their Unicode code point. You can determine the code point of characters using Python’s built-in ord function. For example to calculate the code point for “z” you would use the following code:
"""
ord("z")
"""
# Try this in script.py using print statements:
# - What is the code point of “a”?
# - What about “ “?
# - What about “A”?

print(ord('a'))
print(ord(' '))
print(ord('A'))

# You may have noticed that the uppercase letters have values less than their lowercase counterparts. When sorting, we don’t want to take into account the case of the letters. For example, “cats” should come before “Dogs”, even though ord("c") > ord("D") is True.
# We’ll make this happen by converting everything to lowercase prior to comparison. Since we need to do this often, lets save the lowercase author and title as attributes while loading the bookshelf in utils.py:
# book['author_lower']
# book['title_lower']

# As we noted, our books are pretty close to being sorted by title. From the sorting lessons, you may remember that bubble sort performs well for nearly sorted data such as this.
# The code for performing bubble sort on an array of numbers is provided in sorts.py. However, we are sorting on books which are Python dictionaries. Further, the owner likes to change the ordering of books daily. To make the sort order flexible, add an argument comparison_function. This will allow us to pass in a custom function for comparing the order of two books.

# Our comparison_function will take two arguments, and return True if the first one is “greater than” the second.
# Within the body of the bubble sort function, modify the comparison conditional statement to use the comparison_function instead of the built in operators (if arr[idx] > arr[idx + 1]:).

# Now that we have a bubble sort algorithm that can work on books, let’s give it a shot. Within script.py define a sort comparison function, by_title_ascending.
# It should take book_a and book_b as arguments.
# It should return True if the title_lower of book_a is “greater than” the title_lower of book_b and False otherwise.
def by_title_ascending(book_a, book_b):
  return book_a['title_lower'] > book_b['title_lower']

# Sort the bookshelf using bubble sort. Save the result as sort_1 and print the titles to the console to verify the order.
# How many swaps were necessary?

sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)

for book in sort_1:
  print(book['title'])

# The owner of the bookshop wants to sort by the author’s full name tomorrow. Define a new comparison function, by_author_ascending, within script.py.
# It should take book_a and book_b as arguments.
# It should return True if the author_lower of book_a is “greater than” the author_lower of book_b and False otherwise.
def by_author_ascending(book_a, book_b):
  return book_a['author_lower'] > book_b['author_lower']

# Our sorting algorithms will alter the original bookshelf, so create a new copy of this data, bookshelf_v1.
# This does NOT create a copy:
"""
bookshelf_v1 = bookshelf
"""
bookshelf_v1 = bookshelf[:]

# Try sorting the list of books, bookshelf_v1 using the new comparison function and bubble sort. Save the result as sort_2 and print the authors to the console to verify the order.
# How many swaps are needed now?
sort_2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)

for book in sort_2:
  print(book['author'])

# The number of swaps is getting to be high for even a small list like this. Let’s try implementing a different type of search: quicksort.
# The code for quicksort of a numeric array is in sorts.py. We need to modify it in a similar fashion that we modified bubble sort.
# Add comparison_function as the final argument to the quicksort function.

# Within the quicksort function, be sure to pass the argument for the comparison_function for the recursive calls.

# The last modification we need to make to quicksort is to update the comparison conditional. It is currently using the built in comparison:
"""
if pivot_element > list[i]:
"""
# Update this to use comparison_function.

# Within script.py create another copy of bookshelf as bookshelf_v2.
bookshelf_v2 = bookshelf[:]

# Perform quicksort on bookshelf_v2 using by_author_ascending. This implementation operates on the input directly, so does not return a list.
# Print the authors in bookshelf_v2 to ensure they are now sorted correctly.
sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1, by_author_ascending)

for book in bookshelf_v2:
  print(book['author'])

# The owner has asked for one last sorting order, sorting by the length of the sum of the number of characters in the book and author’s name.
# Create a new comparison function, by_total_length. It should return True if the sum of characters in the title and author of book_a is “greater than” the sum in book_b and False otherwise.
def by_total_length(book_a, book_b):
  return len(book_a['author_lower']) + len(book_a['title_lower']) > len(book_b['author_lower']) + len(book_b['title_lower'])

# Load the long list of books into a new variable, long_bookshelf.
long_bookshelf = utils.load_books('books_large.csv')

long_bookshelf_v1 = long_bookshelf[:]

sort_3 = sorts.bubble_sort(long_bookshelf_v1, by_total_length)

for book in sort_3:
  print(book['author'])

# Comment out the bubble sort attempt and now try quicksort. Does it live up to its name?
long_bookshelf_v2 = long_bookshelf[:]

sorts.quicksort(long_bookshelf_v2, 0, len(bookshelf_v2) - 1, by_author_ascending)

for book in long_bookshelf_v2:
  print(book['author'])