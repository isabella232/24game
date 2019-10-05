import random

''' 24 Game: Use operations on four different numbers to get a result close to 24 '''
def main():
    # Initialize variables to keep track of different states
    newNumbers = True
    highscore = 0

    while True:
        if newNumbers:  # Obtain new four numbers and update the check list
            a = str(random.randint(1, 13))
            b = str(random.randint(1, 13))
            c = str(random.randint(1, 13))
            d = str(random.randint(1, 13))
            newNumbers = False  # Next State
            highscore = 1000 # Reset Highscore
        else:
            # Obtain user input
            print("Valid numbers are", a, b, c, d)
            print("Valid operations are +, -, *, /.")
            print("Enter operations you would like to make or 'r' to reset:")
            print("Format: # / # - # * #, ignore PEMDAS")
            print()
            data = input("Enter Input: ")
            dataList = data.split()  # Separates the inputs into numbers and operations
            correctFormat = False

            while not correctFormat:  # Check if the user input is in correct format
                correctFormat = True  # Input is obtained
                if data == 'r':  # If reset is requested, get new number
                    newNumbers = True
                    break
                elif len(dataList) != 7:  # Make sure there are four numbers and three operations
                    print("Incorrect Format.")
                    print("Format: # / # - # * #, ignore PEMDAS")
                    print()
                    data = input("Enter Input: ")
                    dataList = data.split()
                    print()
                    correctFormat = False  # Format is incorrect so check again

                else:
                    currentPosition = 0  # Keep track of position on list. Numbers are even position
                    numberList = [a, b, c, d]
                    operationList = ['+', '-', '*', '/']
                    for x in dataList:  # Make sure that the four numbers and three operations are correct
                        if currentPosition % 2 == 0:  # Checking a number
                            if x not in numberList:
                                print("Incorrect numbers or format.")
                                print("Valid numbers are", a, b, c, d)
                                print()
                                data = input("Enter Input: ")
                                dataList = data.split()
                                correctFormat = False  # Number is incorrect so check again
                                break  # Break out of for loop and return to while loop
                            else:
                                numberList.remove(x)

                        else:  # Checking an operation
                            if x not in operationList:
                                print("Incorrect operations or format.")
                                print("Valid operations are +, -, *, /.")
                                print()
                                data = input("Enter Input: ")
                                dataList = data.split()
                                correctFormat = False  # Operation is incorrect so check again
                                break  # Break out of for loop and return to while loop
                        currentPosition += 1

            if not newNumbers:  # Obtain result of the input left to right, ignoring PEMDAS
                currentResult = dataList[0], dataList[1], dataList[2]
                currentResult = ' '.join(currentResult)
                currentResult = str(eval(currentResult))

                currentResult = currentResult, dataList[3], dataList[4]
                currentResult = ' '.join(currentResult)
                currentResult = str(eval(currentResult))

                currentResult = currentResult, dataList[5], dataList[6]
                currentResult = ' '.join(currentResult)
                currentResult = eval(currentResult)

                print("Result:", currentResult)
                if currentResult == 24:  # If the value is exactly 24, then obtain new number
                    print("Winner!")
                    newNumbers = True
                else:
                    if abs(currentResult - 24) < highscore:  # Closest to 24 is highscore
                        highscore = abs(currentResult - 24)
                        print("New High Score!")
                    else:
                        print("Try Again!")
                print()

main()
