# 24 game
import random


# input: list to contain the integers and a seed for the random number generator
def genRandomNum(numList, seed):
    random.seed(seed)  # seeds the random number generator for testing purposes
    i = 0
    while i < 4:
        numList.append(random.randint(1, 13))
        i += 1
    return numList


# input: a list containing the expression
# some list of numbers that have been selected
def checkExpression(expression, numList):
    # list of acceptable operators
    operators = ['*', '/', '%', ')', '(', '+', '-', '//', '**']
    # keeps track of the number of parenthises
    openParenthesis = 0
    closedParenthesis = 0

    # checks that the previous is not an operator
    prevIsOperator = False

    # checks that the elements in expression are valid
    for element in expression:
        # checks if the expression is in the list of acceptable operators
        # parentheses are don't change prevIsOperator because they aren't arithmetic operators
        if element in operators:
            if element == '(':
                openParenthesis += 1
            elif element == ')':
                closedParenthesis += 1
            elif prevIsOperator:
                return False
            else:
                prevIsOperator = True
        # checks if the element is a digit
        # checks if the digit was one of the 4 random ones or if it was used already
        # checks to make sure that it isn't a number proceeding another number
        elif element.isdigit():
            # keeps track of numbers that have been used
            availableNumbers = numList[:]
            if not int(element) in availableNumbers:
                return False
            elif not prevIsOperator and len(availableNumbers) != 4:
                return False
            else:
                availableNumbers.remove(int(element))
                prevIsOperator = False
        else:
            return False
    # have to check that the there aren't unpaired parentheses
    return closedParenthesis == openParenthesis


# computes the expression using join and eval
def computeExpression(numList):
    strExpression = "".join(numList)
    return eval(strExpression)


# prints the game's results
def printResults(results):
    if results == 24:
        print("Congratulations!")
    else:
        offset = abs(24 - results)
        print("You were %d off..." % offset)
    return 0


# takes care of determining whether users want to play again
def setPlayAgain():
    while True:
        playAgain = input("Do you want to play again? Enter 'yes' or 'no': ")
        if playAgain == 'yes':
            return True
        elif playAgain == 'no':
            print("Game ended")
            return False
        else:
            print("Please enter 'yes' or 'no'.")


def main():
    print("Starting new game of 24")
    # gets seed from user to seed the random number generator
    seed = int(input("Please enter a seed: "))
    numbers = []
    numbers = genRandomNum(numbers, seed)
    print("Here are your numbers:", end=" ")
    for num in numbers:
        print(num, end=" ")
    print("\n")
    playAgain = True
    while playAgain:
        print("Please enter an expression with a space after every number and operator.")
        expression = input("Enter your expression: ")
        expression = expression.split()
        if checkExpression(expression, numbers):
            results = computeExpression(expression)
            printResults(results)
            playAgain = setPlayAgain()
        else:
            print("Invalid Expression. Please enter a valid one.")
            # print("Make sure you use each number in the list provided only once.")
            # print("Make sure you close all your parenthesis and didn't double you operators.")


main()
