import random
def Hangman1():
    print(" -------  ")
    print(" |    \|  ")
    print("       |  ")
    print("       |  ")
    print("       |  ")
    print("      /|\  ")
def Hangman2():
    print("  -------  ")
    print("  |    \|  ")
    print(" (..)   |  ")
    print("        |  ")
    print("        |  ")
    print("       /|\ ")
def Hangman3():
    print("  -------  ")
    print("  |    \|  ")
    print(" (..)   |  ")
    print("  |     |  ")
    print("        |  ")
    print("       /|\ ")
def Hangman4():
    print("  -------  ")
    print("  |    \|  ")
    print(" (..)   |  ")
    print(" /|     |  ")
    print("        |  ")
    print("       /|\ ")
def Hangman5():
    print("  -------  ")
    print("  |    \|  ")
    print(" (..)   |  ")
    print(" /|\    |  ")
    print("        |  ")
    print("       /|\ ")
def Hangman6():
    print("  -------  ")
    print("  |    \|  ")
    print(" (..)   |  ")
    print(" /|\    |  ")
    print(" /      |  ")
    print("       /|\ ")
def Hangman7():
    print("  -------  ")
    print("  |    \|  ")
    print(" (xx)   |  ")
    print(" /|\    |  ")
    print(" / \    |  ")
    print("       /|\ ")
list_easy = ["autumn", "boy", "girl", "winter", "dance","dripping", "laughing", "wheeze", "lightning", "explosion"]
list_hard = ["jazz", "jazzy", "inertia", "floccinaucinihilipilification", "pneumonoultramicroscopicsilicovolcanoconiosis", "hippopotomonstrosesquipedaliophobia", "antidisestablishmentarianism", "otorhinolaryngological", "immunoelectrophoretically", "psychophysicotherapeutics", "thyroparathyroidectomized", "pneumoencephalographically", "radioimmunoelectrophoresis", "psychoneuroendocrinological", "hepaticocholangiogastrostomy", "spectrophotofluorometrically", "pseudopseudohypoparathyroidism", "zqfmgb"]

greeting = input("Welcome to Dead Man's Letters. The rules are simple: guess the word right, or die. Choose 1 for easy or 2 for hard. ")

if greeting == 1:
    easy_num = random.randint(0, len(list_easy) - 1)
    easy_word = list_easy[easy_num]
    print("*" * len(easy_word))

    noOfTries = 0

    blank = "*" * len(easy_word)
    LBlank = list(blank)

    list_hangman = [Hangman2, Hangman3, Hangman4, Hangman5, Hangman6, Hangman7]

    while noOfTries < 6:
        guess = input("Please guess a letter")
        if guess in easy_word:
            indexes = easy_word.find(guess)
            print (indexes)

            for i in indexes:
                LBlank[i] = guess

            print(''.join(LBlank))
        else:
            print("Incorrect!")
            print list_hangman[noOfTries]()
            noOfTries = noOfTries + 1

    if noOfTries == 6:
        print("Game Over!")
    else:
        print("You win!")


if greeting == 2:
    hard_num = random.randint(0, len(list_hard) - 1)
    hard_word = list_hard[hard_num]
    print("*" * len(hard_word))

    noOfTries = 0

    blank = "*" * len(hard_word)
    LBlank = list(blank)

    list_hangman = [Hangman2, Hangman3, Hangman4, Hangman5, Hangman6, Hangman7]

    while noOfTries < 6:
        guess = input("Please guess a letter")
        if guess in easy_word:
            indexes = hard_word.find(guess)
            print (indexes)

            for i in indexes:
                LBlank[i] = guess

            print(''.join(LBlank))
        else:
            print("Incorrect!")
            print list_hangman[noOfTries]()
            noOfTries = noOfTries + 1

    if noOfTries == 6:
        print("Game Over!")
    else:
        print("You win!")




        sss



        
