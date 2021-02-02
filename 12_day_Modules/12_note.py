# module
# note A module is a file containing a set of codes or a set of functions which can be included to an application.

# note Creating a Module
# note To create a module we write our codes in a python script and we save it as a .py file. Create a file named mymodule.py inside your project folder. Let write some code in this file.
# note Create main.py file in your project directory and import the mymodule.py file.
# note Some of the common built-in modules: math, datetime, os,sys, random, statistics, collections, json,re

import os
import sys
import statistics as sta

# note create a directory
# os.mkdir("test")
# note change current directory
# os.chdir("path")
# note getting current directory
# print(os.getcwd())
# os.rmdir("test")

# to exit sys
# sys.exit()
# To know the largest integer variable it takes
# sys.maxsize
# To know environment path
# sys.path
# To know the version of python you are using
# sys.version

# ages = [20,20,24,24,25,22,26,20,23,22,26]
# print(sta.mean(ages))       # ~22.9
# print(sta.median(ages))     # 23
# print(sta.mode(ages))       # 20
# print(sta.stdev(ages))      # ~2.3

# import math
# print(math.pi)           # 3.141592653589793, pi constant
# print(math.sqrt(2))      # 1.4142135623730951, square root
# print(math.pow(2, 3))    # 8.0, exponential function
# print(math.floor(9.81))  # 9, rounding to the lowest
# print(math.ceil(9.81))   # 10, rounding to the highest
# print(math.log10(100))   # 2, logarithim with 10 as base

# from math import pi, sqrt, pow, floor, ceil, log10
# print(pi)                 # 3.141592653589793
# print(sqrt(2))            # 1.4142135623730951
# print(pow(2, 3))          # 8.0
# print(floor(9.81))        # 9
# print(ceil(9.81))         # 10
# print(log10(100))    # 2

import string
# print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# print(string.digits)        # 0123456789
# print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

import random as rd
print(random())   
# it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20))
# it returns a random integer number between 5 and 20
