word = "bannana"
word_array = []
space_count = 0
count = 0
count_again = 0
ft = True
dead_count = 0
while(space_count < len(word)):
    word_array.append("_")
    space_count+=1

while(count_again < 6):
    letter = input("What letter are you guessing? Put it in quotes. ")
    while (count < len(word)):
        if word[count] == letter:
            word_array[count] = letter
            ft = False

        count += 1
    if ft == True:
        print("Incorrect")
        dead_count += 1
    if dead_count == 7:
        break
        print("Game Over")
    print(word_array)
    count_again +=1
