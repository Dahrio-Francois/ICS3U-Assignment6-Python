#!/usr/bin/env python3

# Created by: Dahrio-Francois
# Created on: May 2022
# This program uses functions to calculate
#   the surface area of a rectangular prism


def calculate_surface_area(length, width, height):
    # calculate area

    # process

    surface_area = 2 * (width * length + height * length + height * width)

    # output

    return surface_area


def main():
    # this function gets the three inputs
    while Exception is not True:
        try:
            # input

            length_from_user = int(
                input("Enter in the length of the rectangular prism: ")
            )
            width_from_user = int(
                input("\nEnter in the width of the rectangular prism: ")
            )
            height_from_user = int(
                input("\nEnter in the height of the rectangular prism: ")
            )

            # call functions
            some_var = calculate_surface_area(
                length_from_user, width_from_user, height_from_user
            )

            print("\nThe total of those three numbers are {} cm²".format(some_var))
            break
        except Exception:
            print("\nThat was not a valid integer, please try again.\n")


if __name__ == "__main__":
    main()
