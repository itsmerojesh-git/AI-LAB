import random

print("Hello, You are welcome to hangman game to guess city name of Nepal")
print("\n")

# List of city names in Nepal
words = ['nepalgunj', 'pokhara', 'bhojpur', 'birtamode', 'dhading']


word = random.choice(words)

print("Guess the characters:")

# List to store guessed characters
guessed_word = []
# Number of chances
chances = 5

# Main game loop
while chances > 0:
    failed = 0
    display_word = ""

    # Create the display word with guessed characters and underscores
    for char in word:
        if char in guessed_word:
            display_word += char
        else:
            display_word += "_"
            failed += 1

    print(display_word)

    # If no underscores are left, the player has won
    if failed == 0:
        print("You Win.")
        print("The word is: ", word + '.')
        break

    # Ask the player to guess a character
    guess = input("Guess a character: ").lower()

    # If the character has already been guessed
    if guess in guessed_word:
        print("You already guessed that character.")
        continue

    # Add the guessed character to the list
    guessed_word.append(guess)

    # If the guessed character is not in the word
    if guess not in word:
        chances -= 1
        print("Wrong")
        print("You have", chances, 'more guesses.')

        # If no chances are left, the player loses
        if chances == 0:
            print("You Lose.")
            print("The word was: ", word + '.')
