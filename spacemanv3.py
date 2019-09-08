import random

# def load_word():
#     file = open('words.txt', 'r')
#     words_list = file.readlines()
#     file.close()

#     words_list = words_list[0].split(' ')
#     secret_word = random.choice(words_list)
#     return secret_word

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
                      't', 'u', 'v', 'w', 'x', 'y', 'z', 
                      '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    user_guesses = []

    print("welcome to spaceman")
    print(number_of_guesses)

    while number_of_guesses > 0:
        user_guess = input("enter a guess: ")

        if len(user_guess) > 1:
            print("you can only guess one letter at a time")
            continue

        if not user_guess.isalpha():
            print("gueeses can be letters only")
            continue

        if user_guess not in all_letters_option:
            print("you already used the letter")
            continue

        if is_guess_in_word(user_guess, secret_word):
            user_guesses.append(user_guess)
            print(user_guesses)
            print("you guessed right")
            print(''.join(get_guessed_word(secret_word, user_guesses)))
        else:
            print("sorry you guess incorrectly")
            print(''.join(get_guessed_word(secret_word, user_guesses)))
            number_of_guesses -= 1
        print(number_of_guesses)

        if is_word_guessed(secret_word, user_guesses):
            print(user_guesses)
            print("you win")
            break

        if user_guess in all_letters_option:
            all_letters_option.remove(user_guess)
            all_letters_updated = ''.join(all_letters_option)
            print("Letters left to guess: " + all_letters_updated)

        if number_of_guesses == 0:
            print("you lose")
            print("the secret word was " + secret_word)
            break

# spaceman(secret_word)



# play = 'y'
# while play == "y":
#     spaceman(secret_word)
#     play = input("y to play")

play = 'y'
while play == 'y':
    # spaceman(load_word())
    spaceman('apple')
    play = input("y to play")


## This is a question of concern
# def is_guess_in_word(guess, secret_word):
#     for letter in secret_word:
#         if letter == guess:
#             return True
#         elif letter != guess:
#             return False
#     # return False 

# list1 = ['a','p','p','l','r']
# if is_guess_in_word('p', 'apple'):
#   print('T')
# else:
#   print('F')