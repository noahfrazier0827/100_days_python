import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
wLen = len(chosen_word)
lives = 6
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print(logo)

display = []

for char in chosen_word:
    display.append("_") 
print(display)

while True:
    guess = input(str.lower(""))

    for position in range(len(chosen_word)):
        char = chosen_word[position]
        if char == guess:
            display[position] = guess
        # elif guess == display[position]:
        #      print(f"youve already used{guess}.")
        # giga cringe dont undersatnd repeat letter fml machinge gun = mom lowkey
    if guess not in chosen_word:
            lives -= 1
            if lives == 0:
                print("Game over.")
                break
    

    print(display)
    
    combined = "".join(display)
    if combined == chosen_word:
        break
