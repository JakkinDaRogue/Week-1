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
list_hard = ["floccinaucinihilipilification", "pneumonoultramicroscopicsilicovolcanoconiosis", "hippopotomonstrosesquipedaliophobia", "antidisestablishmentarianism", "otorhinolaryngological", "immunoelectrophoretically", "psychophysicotherapeutics", "thyroparathyroidectomized", "pneumoencephalographically", "radioimmunoelectrophoresis", "psychoneuroendocrinological", "hepaticocholangiogastrostomy", "spectrophotofluorometrically", "pseudopseudohypoparathyroidism", "zqfmgb"]

dif = input("Welcome to Dead Man's Letters. The rules are simple: guess the word right, or die. Choose 1 for easy or 2 for hard. ")

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


if dif == 1:
    easy_num = random.randint(0, len(list_easy) - 1)
    easy_word = list_easy[easy_num]
    print("_ " * len(easy_word))

    tf = False
    ft = False
    count2 = 0

    blank = "_" * len(easy_word)
    LBlank = list(blank)

    list_hangman = [Hangman2, Hangman3, Hangman4, Hangman5, Hangman6, Hangman7]
    count1 = 0
    while count2 < 6:
            tf = False
            ft = False
            guess = input("Please guess a letter")
            count = 0
            while count < len(easy_word):
                if easy_word[count] == guess:
                    tf = True
                    list_easy[count] = guess
                if guess == easy_word[count]:
                    ft = True
                    print("Correct!")
                    LBlank[count] = guess
                    print(LBlank)
                count = count + 1
            if not ft and not tf:
                print("Incorrect!")
                print list_hangman[count1]()
                count1 = count1 + 1
            if count1 == 3:
                print("Game Over!")
                break

if dif == 2:
    hard_num = random.randint(0, len(list_hard) - 1)
    hard_word = list_hard[hard_num]
    print("_ " * len(hard_word))

    tf = False
    ft = False
    count2 = 0

    blank = "_" * len(hard_word)
    LBlank = list(blank)

    list_hangman = [Hangman2, Hangman3, Hangman4, Hangman5, Hangman6, Hangman7]
    count1 = 0
    while count2 < 6:
            tf = False
            ft = False
            guess = input("Please guess a letter")
            count = 0
            while count < len(hard_word):
                if hard_word[count] == guess:
                    tf = True
                    list_hard[count] = guess
                if guess == hard_word[count]:
                    ft = True
                    print("Correct!")
                    LBlank[count] = guess
                    print(LBlank)
                count = count + 1
            if not ft and not tf:
                print("Incorrect!")
                print list_hangman[count1]()
                count1 = count1 + 1
            if count1 == 3:
                print("Game Over!")
                break

if dif == "import antigravity":
    import antigravity
