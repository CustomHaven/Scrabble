# https://www.codecademy.com/courses/learn-python-3/projects/scrabble
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Q15 accomudate lowercase letters and point*=2 
# so we give each lowercase letter same value as its uppercase letter 
# point*=2 is weird but A: 1 and therefore a: 1 it works and Z: 10 same as z: 10!
letters += [
  letter.lower()
  for letter in letters
]
points *= 2

# Q1
letter_to_points = {key: value for key, value in zip(letters, points)}

# print(letter_to_points)

# Q2
letter_to_points[" "] = 0

# Q3 Q4 Q5 Q6
def score_word(word):
  point_total = 0
  for i in word:
    point_total += letter_to_points.get(i, 0)
  return point_total


# Q7
brownie_points = score_word("BROWNIE")

# Q8
# print(brownie_points)

# Q9
player_to_words = {
  "player1": ["BLUE", "TENNIS", "EXIT"],
  "wordNerd": ['EARTH', 'EYES', 'MACHINE'],
  'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'],
  'Prof Reader': ['ZAP', 'COMA', 'PERIOD']
}
# Q10
player_to_points = {}
# Q11 Q12 Q13 and Q15 told us to make the loop into a function
def update_point_totals():
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points

update_point_totals()
# Q14
print(player_to_points)


# Q15
def play_word(player, word):
  val = player_to_words.get(player, 0)
  if val == 0:
    player_to_words[player] = word
  else:
    player_to_words[player].append(word)
  update_point_totals()

play_word("player1", "wordss")

# print(player_to_words)

# FINALLY
print(player_to_points)