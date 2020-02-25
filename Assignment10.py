# -*- coding: utf-8 -*-
"""
Muhammad Mashwani
PeopleSoft ID: 1378052
Assignment #10
"""
#import os.path
from os import path
from string import ascii_lowercase

letterCount = {}
letterFrequency = {}
totalCount = 0

for c in ascii_lowercase:
    letterCount[c] = 0
for num in range(0,25):
    letterCount[num] = 0
    
if path.exists("words.txt"):
    file1 = open("words.txt","r")
    
    while 1:
        char = file1.read(1)
        if not char: break
        totalCount = totalCount + 1
        char = char.lower()
        if char in letterCount.keys():
            letterCount[char] = letterCount[char] + 1
    
    for c in ascii_lowercase:
        totalCount = totalCount + letterCount[c]
    for c in ascii_lowercase:
        letterFrequency[c] = 100 * (letterCount[c]/(((totalCount-1)/2) - 292500))
        if letterFrequency[c] < 10:
            print(c + " = 0" + "{:.3f}".format(letterFrequency[c]),"%")
        else:
            print(c + " = " + "{:.3f}".format(letterFrequency[c]),"%")
    
    file1.close()

else:
    print("Warning! File does not exist")
    
print(totalCount)            

