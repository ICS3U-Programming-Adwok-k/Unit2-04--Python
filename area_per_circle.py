#!/usr/bin/env python3
# Created by: Adowk Adiebo
# Created on: Mar 8th 28th, 2025
# This program calculates the Area
# and Circumference of a circle.
import math


def main():
    # Input
    radius = float(input("Enter the radius of the circle: "))
    # Process
    Area = math.pi * radius**2
    Circumference = 2 * math.pi * radius
    # Output
    print("The Area of the circle is:  {:,.2f}cm^2".format(Area))
    print("The Circumference of the circle is: {:,.2f}cm".format(Circumference))


if __name__ == "__main__":
    main()
