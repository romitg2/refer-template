#!/usr/bin/env python3

import sys
import re

def getKeywords(content):
    keywords = []

    running = ""
    open = False
    count = 0
     
    for c in content:
        if c == '_':
            count += 1
        else:
            count = 0

        if count == 2:
            if open:
                running = running[:-1]
                if running not in keywords:
                    keywords.append(running)
                running = ""
                open = False
            else:
                open = True

        elif open:
            running += c
    return keywords

if __name__ == "__main__":

    templateFile = ""
    if len(sys.argv) > 1:
        templateFile = sys.argv[1]
        if not templateFile.endswith(".txt"):
            templateFile = templateFile + ".txt"
    else:
        templateFile = "t1.txt"

    content = "";
    with open("./templates/" + templateFile, 'r') as file:
        content = file.read()
    
    name = input("Enter the name of the file: ")

    filename = name;
    filename = filename + ".txt"
    with open(filename, 'w') as file:
        file.write(content)
        file.write(filename)
    
    keywords = getKeywords(content)
    mapping = {}
    for key in keywords:
        mapping[key] = input(key + ": ")

    for key, value in mapping.items():
        content = content.replace("__" + key + "__", value)

    print(content)

