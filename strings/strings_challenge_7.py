# Every Other Letter

# Create a function named every_other_letter that takes a string named word as a parameter. The function should return a string containing every other letter in word.

def every_other_letter(word):
  letters = ''
  for index in range(0, len(word), 2):
    letters = letters + word[index]
  return letters

print(every_other_letter("Codecademy"))

print(every_other_letter("Hello world!"))

print(every_other_letter(""))