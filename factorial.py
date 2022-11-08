#!/usr/bin/env python3

# Created by: Van Nguyen
# Created on: October 31, 2022
# This program asks the user for a positive number and
# uses a do while loop to add up/calculate the factorial
# It will then display the factorial to the user


def main():
    # Initialize Variables
    loop_counter = 0
    factorial_number = 1

    print("NUMBER FACTORIAL CALCULATOR")

    # Asks user for an integer
    user_number_string = input("Enter a positive integer: ")

    # Checks for exceptions
    try:
        # Converts user number to integer
        user_number = int(user_number_string)

    # In the event of an exception
    except:
        print(f"{user_number_string} is not a whole positive number!")

    # If there are no exceptions
    else:

        # IF the user enters a negative number
        if user_number < 0:
            print(f"{user_number} is not a positive number!")

        # IF the user enters an actual valid number
        else:

            # *Do-While Loop Workaround to calculate the factorial of the user number
            while True:

                # Increments loop counter
                loop_counter += 1

                # Displays how many times the program has used this loop
                print(f"Tracking {loop_counter} times through the loop.")

                # Multiplies the integers before the user number by the user number
                factorial_number *= loop_counter

                # *Do-While Loop Workaround condition (ensures loop counter has not passed user number)
                if loop_counter >= user_number:
                    break

            # Displays the factorial to the user
            print(f"{user_number}! = {factorial_number}")


if __name__ == "__main__":
    main()
