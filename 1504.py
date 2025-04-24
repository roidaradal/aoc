# Advent of Code 2015 Day 04
# John Roy Daradal 

from lib import * 

def data(full: bool) -> list[str]:
    return readLines(15, 4, full)

def part1():
    full = True 
    for key in data(full):
        solve(key, 5)

def part2():
    full = True 
    for key in data(full):
        solve(key, 6)

def solve(key: str, numZeros: int):
    goal = '0' * numZeros 
    i = 0 
    while True:
        i += 1
        word = '%s%d' % (key, i)
        hash = md5Hash(word)
        if hash[:numZeros] == goal:
            print(i)
            break

if __name__ == '__main__':
    do(part1)
    do(part2)

'''
Solve:
- Combine key + i and get md5 hash 
- If hash starts with N zeros, output i's value
- Else, Increment i and repeat until goal found
'''