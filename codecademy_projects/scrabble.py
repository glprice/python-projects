letters = [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

points = [0, 1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

player_to_words = {
    "player1": ["BLUE", "TENNIS", "EXIT"],
    "wordNerd": ["EARTH", "EYES", "MACHINE"],
    "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
    "Prof Reader": ["ZAP", "COMA", "PERIOD"]
}

# pairs letters to corresponding points
letter_to_points = {letter: point for letter, point in  zip(letters,points)}

# Calculates points per letter in a word
def score_word(word):
  point_total = 0
  for letter in word.upper():
    point_total += letter_to_points.get(letter,0)
  return point_total

# test of score_word
brownie_points = score_word("Brownie")

player_to_points = {}

# calculates points of players in player_to_words
for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points