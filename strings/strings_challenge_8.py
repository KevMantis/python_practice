# Reverse

# Write a function named reverse_string that has a string named word as a parameter. The function should return word in reverse.

def reverse_string(word):
  word_split = word.split(' ')
  reversed_word = ''
  for index in range(len(word), 0, -1):
    reversed_word = reversed_word + word[index - 1]
  return reversed_word

print(reverse_string("Codecademy"))

print(reverse_string("Hello world!"))

print(reverse_string(""))