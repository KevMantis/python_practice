# Scrabble

# In this project, you will process some data from a group of friends playing scrabble. You will use dictionaries to organize players, words, and points.
# There are many ways you can extend this project on your own if you finish and want to get more practice!
# If you get stuck during this project or would like to see an experienced developer work through it, click “Get Help“ to see a project walkthrough video.
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# We have provided you with two lists, letters and points. We would like to combine these two into a dictionary that would map a letter to its point value.
# Using a list comprehension and zip, create a dictionary called letter_to_points that has the elements of letters as the keys and the elements of points as the values.
letter_to_points = {letter: point for letter, point in zip(letters, points)}

# Our letters list did not take into account blank tiles. Add an element to the letter_to_points dictionary that has a key of " " and a point value of 0.
letter_to_points[' '] = 0

# We want to create a function that will take in a word and return how many points that word is worth.
# Define a function called score_word that takes in a parameter word.
def score_word(word):
  # Inside score_word, create a variable called point_total and set it to 0.
  point_total = 0
  # After defining point_total, create a for loop that goes through the letters in word and adds the point value of each letter to point_total.
  # You should get the point value from the letter_to_points dictionary. If the letter you are checking for is not in letter_to_points, add 0 to the point_total.
  point_total = 0
  for letter in word:
    if letter in letter_to_points:
      point_total += letter_to_points[letter.upper()]
    else:
      point_total += 0
  # After the for loop is finished, return point_total.
  return point_total

# Let’s test this function! Create a variable called brownie_points and set it equal to the value returned by the score_word() function with an input of "BROWNIE".
brownie_points = score_word('BROWNIE')

# We expect the word BROWNIE to earn 15 points:
# (B + R + O + W + N + I + E)
# (3 + 1 + 1 + 4 + 4 + 1 + 1) = 15
# Let’s print out brownie_points to make sure we got it right.
print(brownie_points)

# Create a dictionary called player_to_words that maps players to a list of the words they have played. This table represents the data to transcribe into your dictionary:
player_to_words = {'player1': ['BLUE', 'TENNIS', 'EXIT'], 'wordNerd': ['EARTH', 'EYES', 'MACHINE'], 'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'], 'Prof Reader': ['ZAP', 'COMA', 'PERIOD']}

# Create an empty dictionary called player_to_points.
player_to_points = {}

# Iterate through the items in player_to_words. Call each player player and each list of words words.
# Within your loop, create a variable called player_points and set it to 0.
for player, words in player_to_words.items():
  player_points = 0
  # Within the loop, create another loop that goes through each word in words and adds the value of score_word() with word as an input.
  for word in words:
    player_points += score_word(word)
  # After the inner loop ends, set the current player value to be a key of player_to_points, with a value of player_points.
  player_to_points[player] = player_points

# player_to_points should now contain the mapping of players to how many points they’ve scored. Print this out to see the current standings for this game!
# If you’ve calculated correctly, wordNerd should be winning by 1 point.
print(player_to_points)

# If you want extended practice, try to implement some of these ideas with the Python you’ve learned:
# - play_word() — a function that would take in a player and a word, and add that word to the list of words they’ve played
# - update_point_totals() — turn your nested loops into a function that you can call any time a word is played
# - make your letter_to_points dictionary able to handle lowercase inputs as well