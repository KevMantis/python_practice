# Substring Between

# Write a function named substring_between_letters that takes a string named word, a single character named start, and another character named end. This function should return the substring between the first occurrence of start and end in word. If start or end are not in word, the function should return word.

# For example, substring_between_letters("apple", "p", "e") should return "pl".

def substring_between_letters(word, start, end):
  start_index = word.find(start)
  end_index = word.find(end)
  if start in word and end in word:
    return word[start_index + 1:end_index]
  else:
    return word

print(substring_between_letters("apple", "p", "e"))

print(substring_between_letters("apple", "p", "c"))