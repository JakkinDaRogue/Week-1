operation = input("Hello, and welcome to Jackson's Ultimate Calculator. Press 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division, 5 for powers, 6 for remainders, 7 for min-max, and 8 for base converters. ")

def addition(a, b):
    pass
    c = a + b
    c_str = str(c)
    print("Your answer is " + c_str + ".")

def subtraction(a, b):
    pass
    c = a - b
    c_str = str(c)
    print("Your answer is " + c_str + ".")

def multiply(a, b):
    pass
    d=0
    c=0
    while d < b:
        c = c + a
        d = d + 1
    c_str = str(c)
    print("Your answer is " + c_str + "." )

def divide(a, b):
    pass
    c=0
    while a>=b:
        a = a - b
        c = c + 1
    c_str = str(c)
    print("Your answer is " + c_str + ".")

def power(a, b):
    pass
    d=1
    c=0
    while d < b:
        a = a * a
        c = a
        d = d + 1
    c_str = str(c)
    print("Your answer is " + c_str + ".")

def remainder(a, b):
    pass
    c=0
    while a>=b:
        a = a - b
        c = c + 1
    a_str = str(a)
    print("The remainder is  " + a_str + ".")

#Minmax unfinished
def minmax():
    pass
    count = 0

def BinToDec():
    pass
    count = 0
    ans = 0
    binary = input("What binary number do you want to convert to decimal? ")
    binary_str = str(binary)
    while count <= len(binary_str):
        rem = binary % 2
        ans = rem*2**count + ans
        binary = binary / 10
        count = count + 1
    print(ans)

def BinToOct():
    binary = input("What binary number do you want to convert to octal? ")
    output1 = ""
    output2 = ""
    count = 0
    [side_a, side_b] = str(binary).split(".")

        if len(side_a) % 3 == 1:
            side_a = "00" + side_a
        elif len(side_a) % 3 == 2:
            side_a = "0" + side_a

        if len(side_b) % 3 == 1:
                side_b = side_b + "00"
        elif len(side_b) % 3 == 2:
                side_b = side_b + "0"

        for index in range(0, len(side_a), 3):
            cur_group = side_a[index: index+3]
            if cur_group == "000":
                output1 = output1 + "0"
            elif cur_group == "001":
                output1 = output1 + "1"
            elif cur_group == "010":
                output1 = output1 + "2"
            elif cur_group == "011":
                output1 = output1 + "3"
            elif cur_group == "100":
                output1 = output1 + "4"
            elif cur_group == "101":
                output1 = output1 + "5"
            elif cur_group == "110":
                output1 = output1 + "6"
            elif cur_group == "111":
                output1 = output1 + "7"

        for index in range(0, len(side_b), 3):
            cur_group = side_b[index: index+3]
            if cur_group == "000":
                output2 = output2 + "0"
            elif cur_group == "001":
                output2 = output2 + "1"
            elif cur_group == "010":
                output2 = output2 + "2"
            elif cur_group == "011":
                output2 = output2 + "3"
            elif cur_group == "100":
                output2 = output2 + "4"
            elif cur_group == "101":
                output2 = output2 + "5"
            elif cur_group == "110":
                output2 = output2 + "6"
            elif cur_group == "111":
                output2 = output2 + "7"
        print(output1 + "." + output2)

def BinToHex():
    binary = input("What binary number do you want to convert to hex? ")
    output1 = ""
    output2 = ""
    count = 0
    [side_a, side_b] = str(binary).split(".")

        if len(side_a) % 4 == 1:
            side_a = "000" + side_a
        elif len(side_a) % 4 == 2:
            side_a = "00" + side_a
        elif len(side_a) % 4 == 3:
            side_a = "0" + side_a

        if len(side_b) % 4 == 1:
                side_b = side_b + "000"
        elif len(side_b) % 4 == 2:
                side_b = side_b + "00"
        elif len(side_b) % 4 == 3:
                side_b = side_b + "0"

        for index in range(0, len(side_a), 3):
            cur_group = side_a[index: index+3]
            if cur_group == "0000":
                output1 = output1 + "0"
            elif cur_group == "0001":
                output1 = output1 + "1"
            elif cur_group == "0010":
                output1 = output1 + "2"
            elif cur_group == "0011":
                output1 = output1 + "3"
            elif cur_group == "0100":
                output1 = output1 + "4"
            elif cur_group == "0101":
                output1 = output1 + "5"
            elif cur_group == "0110":
                output1 = output1 + "6"
            elif cur_group == "0111":
                output1 = output1 + "7"
            elif cur_group == "1000":
                output1 = output1 + "8"
            elif cur_group == "1001":
                output1 = output1 + "9"
            elif cur_group == "1010":
                output1 = output1 + "A"
            elif cur_group == "1011":
                output1 = output1 + "B"
            elif cur_group == "1100":
                output1 = output1 + "C"
            elif cur_group == "1101":
                output1 = output1 + "D"
            elif cur_group == "1110":
                output1 = output1 + "E"
            elif cur_group == "1111":
                output1 = output1 + "F"

        for index in range(0, len(side_a), 3):
            cur_group = side_a[index: index+3]
            if cur_group == "0000":
                output1 = output1 + "0"
            elif cur_group == "0001":
                output1 = output1 + "1"
            elif cur_group == "0010":
                output1 = output1 + "2"
            elif cur_group == "0011":
                output1 = output1 + "3"
            elif cur_group == "0100":
                output1 = output1 + "4"
            elif cur_group == "0101":
                output1 = output1 + "5"
            elif cur_group == "0110":
                output1 = output1 + "6"
            elif cur_group == "0111":
                output1 = output1 + "7"
            elif cur_group == "1000":
                output1 = output1 + "8"
            elif cur_group == "1001":
                output1 = output1 + "9"
            elif cur_group == "1010":
                output1 = output1 + "A"
            elif cur_group == "1011":
                output1 = output1 + "B"
            elif cur_group == "1100":
                output1 = output1 + "C"
            elif cur_group == "1101":
                output1 = output1 + "D"
            elif cur_group == "1110":
                output1 = output1 + "E"
            elif cur_group == "1111":
                output1 = output1 + "F"

##################################################################################################################################################################################################################

#Addition
if operation == 1:
    a, b = input("What two numbers would you like to add? Please put a comma between the numbers. ")
    addition(a, b)

#Subtraction
if operation == 2:
    a, b = input("What two numbers would you like to subtract? Please put a comma between the numbers. ")
    subtraction(a, b)

#Multiplication
if operation == 3:
    a, b = input("What two numbers would you like to multiply? Please put a comma between the numbers. ")
    multiply(a, b)

#Division
if operation == 4:
    a, b = input("What two numbers would you like to divide? Please put a comma between the numbers. ")
    divide(a, b)

#Powers
if operation == 5:
    a, b = input("What number would you like a power of? The exponent will be second. Please put a comma between the numbers. ")
    power(a, b)

#Remainder
if operation == 6:
    a, b = input("What two numbers would you like the remainder of? Please put a comma between the numbers. ")
    remainder(a, b)

#Min-Max
if operation == 7:
    minmax()

#Number Converter
if operation == 8:
    type = input("What systems would you like to convert: Press 1 for binary to decimal, 2 for binary to octal, or 3 for binary to hex. ")
    if type == 1:
        BintoDec()
    if type == 2:
        BinToOct(binary)
    if type == 3:
