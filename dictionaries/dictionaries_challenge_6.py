# Word Length Dict

# Write a function named word_length_dictionary that takes a list of strings named words as a parameter. The function should return a dictionary of key/value pairs where every key is a word in words and every value is the length of that word.
def word_length_dictionary(words):
  word_length_dictionary = {}
  for word in words:
    word_length_dictionary[word] = len(word)
  return word_length_dictionary

print(word_length_dictionary(["apple", "dog", "cat"]))

print(word_length_dictionary(["a", ""]))