#!/usr/bin/env python3

# Define a method greet_programmer() that takes no arguments. It should output the string "Hello, programmer!" to the terminal with print().
def greet_programmer():
    print("Hello, programmer!")

# Define a method greet() that takes one argument, a name. It should output the string "Hello, name!" (with "name" being whatever value was passed as an argument) to the terminal with print().
def greet(name):
    print("Hello, " + name + "!")

def greet_with_default(name="programmer"):
    print("Hello, " + name + "!")

def add(num1, num2):
    return num1 + num2

def halve(number):
    return number / 2
