# Count Letters

# Write a function called unique_english_letters that takes the string word as a parameter. The function should return the total number of unique letters in the string. Uppercase and lowercase letters should be counted as different letters.

# We’ve given you a list of every uppercase and lower case letter in the English alphabet. It will be helpful to include that list in your function.

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def unique_english_letters(word):
  uniques = []
  for letter in word:
    if letter in letters and letter not in uniques:
      uniques.append(letter)
  return len(uniques)

print(unique_english_letters("mississippi"))

print(unique_english_letters("Apple"))