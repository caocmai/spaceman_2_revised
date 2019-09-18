
# Function to determine if whole word is guessed, letters_guessed is a list
def is_word_guessed(secret_word, letters_guessed):
    for ch in secret_word:
        if ch not in letters_guessed:
            return False
    return True

### Returns True if guess is found in secret word, and False otherwise
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

# # To test functions
def test_is_word_guessed():
    assert is_word_guessed('apple', 'apple') == True
    assert is_word_guessed('apple', 'apply') == False
    # ?Why does this produce an error
    assert type(is_word_guessed('apple', 'apple')) is bool
    assert "test" not in is_word_guessed('apple', 'apple')


def test_is_guess_in_word():
    assert is_guess_in_word('p', 'apple') == True
    # Making so the assert message appears
    assert is_guess_in_word('s', 'apple') == False, "This should return False"


def test_get_guessed_word():
    assert get_guessed_word('apple', 'pple') == ['-', 'p', 'p', 'l', 'e'] 
    assert get_guessed_word('apple', 'pple') != ['-', '-', 'p', 'l', 'e']


if __name__ == "__main__":
    test_is_word_guessed()