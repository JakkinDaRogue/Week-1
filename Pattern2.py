max_wid = input("What is the width of your arrows? ")
arrow_amt = input("How many arrows do you want? ")
x = 0
while arrow_amt >= x:
    while max_wid >= x:
        print ("*" * x)
        x+=1
    while x >= 1:
        print ("*" * x)
        x-=1
    arrow_amt -= 1
