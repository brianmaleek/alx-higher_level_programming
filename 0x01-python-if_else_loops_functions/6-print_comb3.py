#!/usr/bin/python3
for number in range(0, 10):
    for number2 in range(0, 10):
        if number == number2 or number > number2:
            continue
        elif number == 8 and number2 == 9:
            print(f"{number}{number2}")
        else:
            print(f"{number}{number2}, ", end="")
