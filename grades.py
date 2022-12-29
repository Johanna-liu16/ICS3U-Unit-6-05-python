#!/usr/bin/env python3

# Created by: Johanna Liu
# Created on: Dec 2022
# This program calculates the average

def average_mark(marks):
    # This function finds the average

    total = 0

    for mark in marks:
        total += mark

    average = round(total / len(marks), 2)

    return average


def main():
    # This function makes the list

    marks = []
    temp_int = None

    # Input
    print("This program calculates the average grade. Enter -1 to end.")
    print("")

    while True:
        try:
            temp_number = input("What is your mark (0 - 100): ")
            temp_int = int(temp_number)
            if temp_int < 100 and temp_int > 0:
                marks.append(temp_int)
            elif temp_int == -1:
                average = average_mark(marks)
                print("\nThe average is {0}%".format(average))
                break
        except ValueError:
            print("Invalid Input")
            continue

    print("\nDone.")


if __name__ == "__main__":
    main()