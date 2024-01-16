from time import sleep
WORD = "computer"
HANGMAN_PICS = [
'''   +---+
       |
       |
       |
     =====''',
     '''   +---+
   0   |
       |
       |
     =====''',
     '''   +---+
   0   |
   |   |
       |
     =====''',
     '''   +---+
   0   |
   |\\  |
       |
     =====''',
     '''   +---+
   0   |
  /|\\  |
       |
     =====''',
     '''   +---+
   0   |
  /|\\  |
    \\  |
     =====''',
     '''   +---+
   0   |
  /|\\  |
  / \\  |
     =====''',
]

WINNER = [
    '''     +----+
       WI  
       NN  
       ER  
     ======''',
]


def start():
    print("Welcome To Hangman! Word Guess Game")
    print(HANGMAN_PICS[0])

    print("\nGuess the word")
    word_counter = 0
    counter = 1
    while counter < 7:
        guess = input("Guess: ")
        if guess == WORD[word_counter]:
            word_counter += 1
            continue
        print(HANGMAN_PICS[counter])
        counter += 1
        if counter > 6:
            print("You could not guess the word!\n")
            sleep(2)
            menu()
    if counter < 6:
        print("\n",WORD.upper())
        sleep(1)
        print("You have guessed the word... Congratulations")
        print(WINNER[0])
    

def end():
    print('''
        00
       \\__/
''')
    print("Goodbye!")

def menu():
    choice = input("Do you want to play the game:\nyes or no: ").lower()
    if choice in ['yes', 'y']:
        start()
    else:
        end()

menu()