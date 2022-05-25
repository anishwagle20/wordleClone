from rich.prompt import Prompt
from rich.console import Console
from random import choice
import random

#Colored Boxes to append over letter
color = {
    'green': '🟩',
    'yellow': '🟨',
    'black': '⬛'
}

# Called after every Guess until game is over
req = "\n GUESS WORD PLEASE "

#Total number of guess allowed in the game
totalGuess = 6

def find(guess, answer):
    guessed = []
    wordle_pattern = []
    for i, colorChoice in enumerate(guess):
        if answer[i] == guess[i]:
            guessed += f'[black on green]{colorChoice}[/]'
            wordle_pattern.append(color['green'])
        elif colorChoice in answer:
            guessed += f'[black on yellow]{colorChoice}[/]'
            wordle_pattern.append(color['yellow'])
        else:
            guessed += f'[black on white]{colorChoice}[/]'
            wordle_pattern.append(color['black'])
    return ''.join(guessed), ''.join(wordle_pattern)


def wordle(selectedWord):
    end = False
    guessedWord = []
    full = []
    guessedList = []

    while not end:
        guess = Prompt.ask(req).upper()
        if guess.lower() in words:
            while len(guess) != 5 or guess in guessedWord:
                if guess in guessedWord:
                    console.print("[red]PLEASE GUESS NEW WORD\n[/]")
                else:
                    console.print('[red]PLEASE ENTER 5-LETTERS WORD ONLY\n[/]')
                guess = Prompt.ask(req).upper()
            guessedWord.append(guess)
            guessed, pattern = find(guess, selectedWord)
            guessedList.append(guessed)
            full.append(pattern)

            console.print(*guessedList, sep="\n")
            if guess == selectedWord or len(guessedWord) == totalGuess:
                end = True
        else:
            print("INVALID WORD")
            pass
    if len(guessedWord) == totalGuess and guess != selectedWord:
        console.print(f"\n[red]WORDLE X/{totalGuess}[/]")
        console.print(f'\n[green]CORRECT WORD WAS: {selectedWord}[/]')
    else:
        console.print(
            f"\n[green] GUSSED WORD CORRECTLY AT: {len(guessedWord)}/{totalGuess}[/]\n")
   


if __name__ == '__main__':
    console = Console()

#Importing text file and slecting random string from it
    with open("sgb-words.txt", "r") as wordlist:
        text = wordlist.read()
    words = list(map(str, text.split()))
    selectedWord = (random.choice(words))

    print("\n WORDLE CLONE GAME Made By ANISH WAGLE (VIT VELLORE) \n")
    print(" YOU HAVE 5 GUESSES \n 1. If guess letter is in correct place it will marked in Green \n 2. If guess letter is not in correct place but in the word it will be in white color \n 3. If gussed letter is not in the word it will marked in black color")
    wordle(selectedWord.upper())
