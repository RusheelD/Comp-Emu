import os
import sys


def get_bits_from_destination(destination: str):
    destinations = destination.split(',')
    bits = 0
    for dest in destinations:
        dest = dest.strip()
        if 'A' == dest:
            bits |= 4
        if 'D' == dest:
            bits |= 2
        if 'A*' == dest or '*A' == dest:
            bits |= 1
    return bits

def get_jump_bits_from_jump(jump: str):
    jump = jump.strip()
    if(jump == ""):
        return 0
    if(jump == 'JGT'):
        return 1
    if(jump == 'JEQ'):
        return 2
    if(jump == 'JGE'):
        return 3
    if(jump == 'JLT'):
        return 4
    if(jump == 'JNE'):
        return 5
    if(jump == 'JLE'):
        return 6
    if(jump == 'JMP'):
        return 7

def get_op_bits_from_value(value: str):
    op = 0
    
    if(value == 'D' or value == 'A' or value == 'A*' or value == '*A'):
        return 4
    
    if('-' in value):
        operation = value.split('-')
        if(operation[-1].strip() == '1'):
            op |= 7
        else:
            op |= 6
    if('+' in value):
        operation = value.split('+')
        if(operation[-1].strip() == '1'):
            op |= 5
        else:
            op |= 4
    if('~' in value):
        op |= 3
    if('^' in value):
        op |= 2
    if('|' in value):
        op |= 1
    if('&' in value):
        op |= 0
    
    return op

def get_swz_bits_from_value(value: str):
    op = 0
    if(value == '0'):
        return 6
    if(value == 'D'):
        return 4
    if(value == 'A' or value == 'A*' or value == '*A'):
        return 2
    
    if('<<' in value):
        operation = value.split('<<')
        if(operation[0].strip() == ''):
            op |= 2
        if(operation[-1].strip()[0] == 'D'):
            op |= 1
    
    if('>>' in value):
        operation = value.split('<<')
        if(operation[0].strip() == ''):
            op |= 2
        if(operation[-1].strip()[0] == 'D'):
            op |= 1

    if('-' in value):
        operation = value.split('-')
        if(operation[0].strip() == ''):
            op |= 2
        if(operation[-1].strip()[0] == 'D'):
            op |= 1
    if('+' in value):
        operation = value.split('+')
        if(operation[0].strip() == ''):
            op |= 2
        if(operation[-1].strip()[0] == 'D'):
            op |= 1
    if('~' in value):
        operation = value.split('~')
        if(operation[-1].strip()[0] != 'D'):
            op |= 1
    if('^' in value):
        operation = value.split('^')
        if(operation[0].strip() == ''):
            op |= 2
        if(operation[-1].strip()[0] == 'D'):
            op |= 1    
    if('|' in value):
        operation = value.split('|')
        if(operation[0].strip() == ''):
            op |= 2
        if(operation[-1].strip()[0] == 'D'):
            op |= 1
    if('&' in value):
        operation = value.split('&')
        if(operation[0].strip() == ''):
            op |= 2
        if(operation[-1].strip()[0] == 'D'):
            op |= 1
    
    return op

def get_shift_from_value(value: str):
    sh = 0
    if '<<' in value or '>>' in value:
        sh |= 2
    if '>>' in value:
        sh |= 1
    
    return sh

def get_sel_from_value(value: str):
    if 'A*' in value or '*A' in value:
        return 1
    return 0

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

lines = []
with open(filename, 'r') as f:
    for line in f.readlines():
        jump = get_jump_condition(line)
        value = get_value(line)
        destination = get_destination(line)
        dest_bits = get_bits_from_destination(destination)
        shift_bits = get_shift_from_value(value)
        sel_bit = get_sel_from_value(value)
        jump_bits = get_jump_bits_from_jump(jump)
        op_bits = get_op_bits_from_value(value)
        swz_bits = get_swz_bits_from_value(value)
        inst = 0 if destination == 'A' and value.isdecimal() and jump_bits == 0 else 1

        # print(destination, ",", value, ",", jump, ",", bin(dest_bits), ",", bin(jump_bits))
        instruction = inst << 15 | shift_bits << 13 | sel_bit << 12 | op_bits << 9 | swz_bits << 6 | dest_bits << 3 | jump_bits
        
        line = instruction if inst else int(value)
        lines.append(line)

with open(filename.split('.')[0] + '-assembled.txt', 'w') as f:
    f.write('[' + str(lines[0]) + ']' + '\n')
    for line in lines[1:]:
        f.write('+ [' + str(line) + ']' + '\n')
