a = "bannana"
word_array = []
space_count = 0
count = 0
dead_count = 0
tf = False
ft = False
while(space_count < len(a)):
    word_array.append("_")
    space_count += 1

while(count < 7):
    letter = input("What letter are you guessing? Put it in quotes. ")
    while (count < len(a)):
        if a[count] == letter:
            tf = True
            word_array[count] = letter
            print("Correct")
            count += 1
            
    if tf != True:
        print("Incorrect")
        dead_count += 1
    print(word_array)
