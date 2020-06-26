# Count First Letter

# Create a function named count_first_letter that takes a dictionary named names as a parameter. names should be a dictionary where the key is a last name and the value is a list of first names. For example, the dictionary might look like this:
# names = {"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}
# The function should return a new dictionary where each key is the first letter of a last name, and the value is the number of people whose last name begins with that letter.
# So in example above, the function would return:
# {"S" : 4, "L": 3}
def count_first_letter(names):
  new_dictionary = {}
  for key, value in names.items():
    if key[0] in new_dictionary.keys():
      count = 0
      for name in value:
        count += 1
      new_dictionary[key[0]] += count
    else:
      new_dictionary[key[0]] = len(value)
  return new_dictionary

print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))

print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))