import random

import hangman_words

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

import hangman_art

print(hangman_art.logo)

print("word to guess: ", end="")
for _ in range(word_length):
    print("_", end="")
print("")

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"{guess} is already guessed.")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The word is {chosen_word}")
        elif guess not in chosen_word:
            print(f"{guess} is not in the word, you lose a life.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    stages = hangman_art.stages
    print(stages[lives])
