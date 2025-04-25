# Advent of Code 2016 Day 05
# John Roy Daradal 

from lib import * 

def data(full: bool) -> str:
    return readLines(16, 5, full)[0]

def part1():
    full = True 
    door = data(full)
    i = 0
    pwd = []
    for _ in range(8):
        while True:
            key = '%s%d' % (door,i)
            i += 1
            hash = md5Hash(key)
            if hash[:5] == '00000':
                pwd.append(hash[5])
                break
    print(''.join(pwd))

def part2():
    full = True 
    door = data(full)
    indexes = [str(x) for x in range(8)]
    pwd = ['.'] * 8 
    i = 0 
    while any(p == '.' for p in pwd): 
        key = '%s%d' % (door,i)
        i += 1 
        hash = md5Hash(key)
        if hash[:5] == '00000' and hash[5] in indexes:
            idx = int(hash[5])
            if pwd[idx] == '.':
                pwd[idx] = hash[6]
                print(''.join(pwd))

if __name__ == '__main__':
    do(part1)
    do(part2)

'''
Part1:
- Increment i until you find an md5Hash of (doorI) that starts with 00000
- Each time you find a valid hash, add the 6th character to the password string
- Continue with the next i after finding a password character
- Repeat 8 times to complete the password 

Part2:
- Initialize password to all '.' 
- Similar processing as in Part 1 
- If hash is valid (starts with 00000), check if 6th character is a valid password index 
- If password index is still '.', replace with the 7th hash character
- Repeat until password has no more '.'
'''