import random
import string


class WordBank:
    """Holds candidate words and picks one at random."""

    DEFAULT_WORDS = [
        "python", "variable", "function", "iterator", "notebook",
        "pipeline", "dataset", "computer", "research", "analytics"
    ]

    def __init__(self, words=None):
        self.words = words or self.DEFAULT_WORDS

    def get_random_word(self):
        return random.choice(self.words)


class GuessBoard:
    """Tracks the secret word, revealed letters, and used guesses."""

    def __init__(self, word):
        self.word = word
        self.blanks = ["_" for _ in word]
        self.used_letters = set()

    def reveal_letters(self, letter):
        """Reveal all occurrences of letter; return True if any were found."""
        found_any = False
        for i, ch in enumerate(self.word):
            if ch == letter and self.blanks[i] == "_":
                self.blanks[i] = letter
                found_any = True
        return found_any

    def mark_used(self, letter):
        self.used_letters.add(letter)

    def is_used(self, letter):
        return letter in self.used_letters

    def is_complete(self):
        return "_" not in self.blanks

    def display(self):
        return " ".join(self.blanks)


class InputHandler:
    """Handles collecting valid letter guesses from the player."""

    @staticmethod
    def prompt_for_letter(board):
        while True:
            guess = input("Guess a letter: ").strip().lower()
            if len(guess) != 1 or guess not in string.ascii_lowercase:
                print(" → Please enter a single A-Z letter.")
                continue
            if board.is_used(guess):
                print(" → You already tried that letter.")
                continue
            return guess


class WordGuessGame:
    """Orchestrates a full round of the word guessing game."""

    def __init__(self, max_lives=6, word_bank=None):
        self.max_lives = max_lives
        self.word_bank = word_bank or WordBank()
        self.lives = max_lives
        self.board = None

    def _setup(self):
        secret = self.word_bank.get_random_word()
        self.board = GuessBoard(secret)
        self.lives = self.max_lives

    def _handle_guess(self, guess):
        self.board.mark_used(guess)

        if self.board.reveal_letters(guess):
            print("\n Well done, Nice job! You found a letter.")
            print(self.board.display())
            if self.board.is_complete():
                self._win()
                return True
        else:
            self.lives -= 1
            print(f"\nNope. You lose a life. Lives left: {self.lives}")
            print(self.board.display())
            if self.lives <= 0:
                self._lose()
                return True

        return False

    def _win(self):
        print("\n Congratulation! You guessed the word!")
        print(f"Word: {self.board.word}")
        print("GAME OVER")

    def _lose(self):
        print("\n Out of lives & Sad story!")
        print(f"The word was: {self.board.word}")
        print("GAME OVER")

    def play(self):
        self._setup()
        print("\nWelcome to Word Guessing!")
        print(f"The word has {len(self.board.word)} letters.")
        print(self.board.display())

        game_over = False
        while not game_over:
            guess = InputHandler.prompt_for_letter(self.board)
            game_over = self._handle_guess(guess)


if __name__ == "__main__":
    WordGuessGame().play()