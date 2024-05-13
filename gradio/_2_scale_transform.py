"""
Filename: _2_scale_transform.py <br>
Title: Custom scale transformer for new user input <br>
Author: Raghava | GitHub: @raghavtwenty <br>
Date Created: June 10, 2023 | Last Updated: May 13, 2024 <br>
Language: Python | Version: 3.10.14, 64-bit <br>
"""

# Importing required library
import numpy as np


# Transformation function
def transform_new_input(new_input):

    # Scaled minimum and maximum values from preprocessing
    scaled_min = np.array(
        [
            1.0,
            10.0,
            856.0,
            5775.0,
            42.0,
            26.0,
            0.0,
            278.0,
            4.0,
            1.0,
            -630355.0,
            4.0,
            50.0,
        ]
    )

    scaled_max = np.array(
        [
            4.0,
            352752.0,
            271591638.0,
            239241314.0,
            421552.0,
            3317.0,
            6302708.0,
            6302708.0,
            5.0,
            5.0,
            1746749.0,
            608.0,
            1012128.0,
        ]
    )

    new_input = np.array(new_input)

    # Formula for transformation
    scaled_input = (new_input - scaled_min) / (scaled_max - scaled_min)

    return scaled_input


# Main
if __name__ == "__main__":
    # Test case
    test_input = [
        [2, 209, 20671, 6316631, 274, 96, 3527, 2757949, 5, 2, 183877, 8, 90494]
    ]

    print("Scaled value: ")
    print(transform_new_input(test_input))
