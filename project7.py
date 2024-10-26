import random
from hangman_art import stages, logo2, logo3
from hangman_words import word_list

# Welcome Message
print(logo3)

# Generate Word
chosen_word = random.choice(word_list)

# Placeholder Sections
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_ "
print(placeholder)

# Game Status
correct_letters = []
lives = 6
game_over = False

# The Game
while not game_over:
    print(f"You have {lives} lives!")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")
    
    
    display = ""
    for char in chosen_word:
        if char == guess:
            display += char
            correct_letters.append(char)
        elif char in correct_letters:
            display += char
        else:
            display += "_ "

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You've guessed {guess}, That is not in the word. You lose a life.")

        if lives == 0:
            game_over = True
            print(f"IT WAS {chosen_word} You Lose")

    if "_" not in display:
        print("YOU WON")
        game_over = True

    print(stages[lives])