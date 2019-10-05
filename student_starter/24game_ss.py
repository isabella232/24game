# TODO Add necessary Library

''' 24 Game: Use operations on four different numbers to get a result close to 24 '''


def main():
    # Initialize variables to keep track of different states
    newNumbers = True
    highscore = 0

    while True:
        if newNumbers:
            # TODO Get New Numbers
            newNumbers = False  # Next State
            highscore = 1000  # Reset Highscore
        else:
            print("Valid numbers are:")  # TODO Display New Numbers
            print("Valid operations are: +, -, *, /.")
            print("Enter operations you would like to make or 'r' to reset:")
            print("Format: # / # - # * #, ignore PEMDAS")
            print()
            # TODO Get Input Data
            correctFormat = False

            while not correctFormat:  # Check if the user input is in correct format
                correctFormat = True  # Placeholder
                # TODO Check Input Format

            if not newNumbers:  # Obtain result of the input left to right, ignoring PEMDAS
                newNumbers = True  # Placeholder
                # TODO Evaluate Results


main()
