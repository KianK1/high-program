#!/usr/bin/python3
# Define the input string
str1 = "python is an interpreted, interactive, object-oriented programming language that combines remarkable power with very clear syntax"
words = str1.split()
if len(words) > 6:
    target = words[5] + " " + words[6]
    print(target)
