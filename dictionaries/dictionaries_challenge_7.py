# Frequency Count

# Write a function named frequency_dictionary that takes a list of elements named words as a parameter. The function should return a dictionary containing the frequency of each element in words.
def frequency_dictionary(words):
  frequency_dictionary = {}
  for word in words:
    frequency_dictionary[word] = words.count(word)
  return frequency_dictionary

print(frequency_dictionary(["apple", "apple", "cat", 1]))

print(frequency_dictionary([0,0,0,0,0]))