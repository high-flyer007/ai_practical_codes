
# Intelligent Number Guessing Agent using Binary Search

def number_guessing_agent():

    # Initialize the search range
    low = 1
    high = 100

    attempts = 0

    print("Think of a number between 1 and 100.")
    print("I will try to guess your number!")
    print("Enter: Higher, Lower, or Correct.")

    # Continue until the number is guessed
    while low <= high:

        # Calculate the middle number
        guess = (low + high) // 2

        attempts += 1

        print("\nMy Guess:", guess)

        # Get feedback from the user
        feedback = input(
            "Is your number Higher, Lower, or Correct? "
        ).lower().strip()

        # Check the feedback
        if feedback == "correct":

            print("\nI guessed your number!")
            print("Correct Number:", guess)
            print("Total Attempts:", attempts)
            break

        elif feedback == "higher":

            # Secret number is greater than the guess
            low = guess + 1

        elif feedback == "lower":

            # Secret number is smaller than the guess
            high = guess - 1

        else:

            print("Invalid input! Please enter Higher, Lower, or Correct.")

    else:
        print("\nYour feedback was inconsistent.")
        print("No possible number remains in the search range.")


# Main program
number_guessing_agent()
