import random

def load_word():
    file = open('words.txt', 'r')
    words_list = file.readlines()
    file.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

# Function to determine if whole word is guessed, letters_guessed is a list
def is_word_guessed(secret_word, letters_guessed):
    for ch in secret_word:
        if ch not in letters_guessed:
            return False
    return True

# To determine if letter guessed is in secret word
# def is_guess_in_word(guess, secret_word):
#     for letter in secret_word:
#         if letter == guess: # This must have 'letter' because it follows previous
#             return True
#     return False # Why here and not indented, when indent doesn't work

### This does work!!
def is_guess_in_word(guess, secret_word):
    if secret_word.find(guess) != -1:
        return True
    else:
        return False

# To populate a list of guessed and non guessed('-') letters
def get_guessed_word(secret_word, letters_guessed):
  letters_guess_so_far = []
  for letter in secret_word:
    if letter in letters_guessed:
      letters_guess_so_far.append(letter)
    else:
      letters_guess_so_far.append('-')
  return letters_guess_so_far


def spaceman(secret_word):
    number_of_guesses = len(secret_word)
    all_letters_option = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
                    'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                      't', 'u', 'v', 'w', 'x', 'y', 'z']
    user_guesses = [] # This is a list of correct guesses

    print("\nWelcome to spaceman".upper())
    print(f'There are {number_of_guesses} letters in the secret word. You have {number_of_guesses} incorrect guesses'.upper())
    print("The secret word:" + ''.join(get_guessed_word(secret_word, user_guesses)))

    while number_of_guesses > 0:
        print("===============================================================")
        print("You have " + str(number_of_guesses) + " guesse(s) left")
        
        user_guess = input("Enter a guess: ")

        if len(user_guess) != 1:
            print("You can only guess one letter at a time".upper())

        if not user_guess.isalpha():
            print("Gueeses can be letters only".upper())
            continue

        if user_guess not in all_letters_option:
            print("You already guessed the letter".upper())
            continue

        if is_guess_in_word(user_guess, secret_word):
            user_guesses.append(user_guess)
            print("Nice. You guessed right")
            print(''.join(get_guessed_word(secret_word, user_guesses)))
            if is_word_guessed(secret_word, user_guesses):
                print("Congradulations! You guessed all the letters. You win".upper())
                print("===============================================================")
                break
        else:
            print("Sorry you guessed incorrectly")
            print(''.join(get_guessed_word(secret_word, user_guesses)))
            number_of_guesses -= 1

        if user_guess in all_letters_option:
            all_letters_option.remove(user_guess)
            all_letters_updated = ''.join(all_letters_option)
            print("Letters left to guess: " + all_letters_updated)

        if number_of_guesses == 0:
            print("Game Over. You are out of guesses. You lose".upper())
            print("The secret word was: ".upper() + secret_word)
            print("===============================================================")
            break

# spaceman(secret_word)



# play = 'y'
# while play == "y":
#     spaceman(secret_word)
#     play = input("y to play")

to_play = 'y'
while to_play == 'y':
    spaceman(load_word())
    # spaceman('apple') # Use this instance to just test out the program
    to_play = input("Type 'y' to play again ")
