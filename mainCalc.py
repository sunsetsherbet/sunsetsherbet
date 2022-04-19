import cube  # imports functions for cubed, squared, and common core calculations
import square
import core



print("*Please input a number 1 - 9 *")
# time.sleep(1)
print("*1. Squared Numbers (Math) ***")  # beginning menu
# time.sleep(1)
print("*2. Cubed Numbers (Math) *****")
# time.sleep(1)
print("*3. Common Core Math (Math) **")
# time.sleep(1)

Question = int(input("Please enter an integer 1-3: ")) # input to activate which calculation the user would like to use
if Question == 1:   # Squared calculations
    U = int(input("Please enter the amount of numbers you would like to square "))
    print('')
    print('1. This is the number squaring port ')
    while U > 0: # iteration
        print('')
        print('')
        print("Please input a number to Square: ")
        square.fun(float(input())) # squared function
        U = U - 1 # subtracts turns by 1 for iteration
elif Question == 2:  # Cubic port calculations
    P = int(input("Please enter number of times you would like to iterate: ")) # number of turns to iterate
    print('')
    print("2. This is the cubic port ")
    print('')
    while P > 0: #iteration of turns
        print('')
        print('')
        print("Please input a number to be cubed: ")
        cube.cub(float(input())) # function to calculate cubed number
        P = P - 1 #turns subtracted by 1 during end of iteration
elif Question == 3:  # Common Core Math
    print('3. This is a common core port ')
    print('Input the number of times you would like to iterate: ')
    iN = int(input()) #number of turns
    while iN > 0: # iteration of turns
        print("Please input one of the following characters that represents mathematical equations ")
        print('(M)ultiplication, (D)ivision, (A)ddition, (S)ubtraction')
        userI = input().upper()
        if userI == "M":
            print("Multiplication Menu:")
            print("Please enter two floats or integers separated by a new line")
            core.multi(float(input()), float(input())) #multiplication function
            iN = iN - 1 #turn subtraction in each if statement
        elif userI == "D":
            print("Division Menu:")
            print("Please enter two numbers separated by a new line")
            core.divis(float(input()), float(input())) # division function
            iN = iN - 1
        elif userI == "A":
            print("Addition Menu:")
            print('Please enter two numbers separated by a new line')
            core.addit(float(input()), float(input())) # addition function
            iN = iN - 1
        elif userI == "S":
            print("Subtraction Menu:")
            print('Please enter two numbers separated by a new line')
            core.subtra(float(input()), float(input())) # subtraction function
            iN = iN - 1
        else:
            print("Didn't get that...") # if incorrect is input then turns are not subtracted by 1
else:
    print('Please enter an integer between 1-3. ')
