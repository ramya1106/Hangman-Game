# Hangman Game - Python

This is a simple **Hangman** game implemented in Python. The game randomly selects a word from a predefined list, and the player has to guess it by suggesting letters within a certain number of attempts.

## Project Structure

The project is made up of three files:

- **`main.py`**: The main code for the Hangman game logic, where the user interacts with the game.
- **`hangman_words.py`**: Contains a list of words to be guessed in the game.
- **`hangman_art.py`**: Contains ASCII art for displaying the hangman stages based on the number of wrong guesses.

## How to Play

1. The game starts by showing an empty word with blanks for each letter.
2. The player guesses one letter at a time.
3. If the letter is in the word, it will fill in the blank.
4. If the letter is not in the word, a part of the hangman is drawn.
5. The game ends when the player either guesses the word correctly or runs out of attempts.

## How to Run the Game

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/hangman-game.git

2. Navigate to the project directory:
   ```bash
    cd hangman-game

3. Make sure you have Python installed.

4. Run the game by executing the following command:
  
   ```bash
    python main.py

## Example Output

    ```text
     _                                             
    | |                                            
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
    | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|  
                        __/ |                       
                       |___/    
    
    Word to guess: _______
    
    Guess a letter: e
    _ _ _ _ _ e _
    
      +---+
      |   |
          |
          |
          |
          |
    =========
    
    Guess a letter: r
    r is not in the word, you lose a life.
    _ _ _ _ _ e _
    
      +---+
      |   |
      O   |
          |
          |
          |
    =========
  

## Dependencies

- Python 3.x

No additional libraries or frameworks are required for this project. It runs entirely using basic Python functionality.

## Contributions

Feel free to fork this repository, improve it, and submit a pull request. Suggestions for improvement are welcome!



