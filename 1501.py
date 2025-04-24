# Advent of Code 2015 Day 01
# John Roy Daradal 

from lib import * 

def data(full: bool) -> list[str]:
    return readLines(15, 1, full)

def part1():
    full = True 
    for line in data(full):
        level = 0
        for x in line: 
            if x == '(': 
                level += 1
            elif x == ')':
                level -= 1
        print(level)

def part2():
    full = True 
    basement = -1
    for line in data(full):
        level = 0 
        for i,x in enumerate(line):
            if x == '(':
                level += 1 
            elif x == ')':
                level -= 1
            if level == basement:
                print(i+1)
                break


if __name__ == '__main__':
    do(part1)
    do(part2)

'''
Part1:
- Iterate through each character in line 
- If ( : increase level by 1 
- If ) : decrease level by 1

Part2:
- Same level processing in Part 1 
- If level == -1: output character index+1
'''