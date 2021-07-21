print('This program tells you whether a number of your choice is divisible by another number of your choice ')
#This is the while loop to keep the program running continuously
while True :
    dividend = int(input("Give me a dividend "))
    divisor = int(input("Give me a divisor "))

    #Gets the remainder of the division between dividend and divisor
    x = dividend % divisor

    #If the remainder is equal to zero
    if x == 0:
        print(dividend, 'is divisible by', divisor, '.')

    #If the remainder is a different number besides zero
    else:
        print(dividend, 'is not divisible by', divisor, '.')

    #Checks if user wants to go out of loop
    exit = input('If you would like to exit this program, press the letter e. If not, then type CONTINUE. ')

    if exit == 'CONTINUE':
        print('Okay! Loading questions . . . thinking of answers . . . ')

    elif exit == 'e' or 'E':
        print('Bye! I hope you liked this program! ')
        break
