# X Length

# Create a function called x_length_words that takes a string named sentence and an integer named x as parameters. This function should return True if every word in sentence has a length greater than or equal to x.

def x_length_words(sentence, x):
  sentence_split = sentence.split(' ')
  for word in sentence_split:
    if len(word) >= x:
      return True
    return False

print(x_length_words("i like apples", 2))

print(x_length_words("he likes apples", 2))