import os
import sys


def get_destination(line: str):
    i = line.find('=')
    if i < 0:
        return ""
    return line[0:i].strip()


def get_jump_condition(line: str):
    i = line.find(';')
    if i < 0:
        return ""
    return line[i+1:].strip()


def get_value(line: str):
    i = line.find('=')
    j = line.find(';')
    if i < 0:
        i = 0
    if j < 0:
        j = len(line)
    return line[i+1:j].strip()


argv = sys.argv

if (len(argv) != 2):
    print("Usage: python assembler.py <filename>")

filename = argv[1]

with open(filename, 'r') as f:
    for line in f.readlines():
        jump = get_jump_condition(line)
        value = get_value(line)
        destination = get_destination(line)

        print(destination, ",", value, ",", jump)
