# Advent of Code 2016 Day 04
# John Roy Daradal 

from lib import * 

class Room:
    def __init__(self, line: str):
        head, tail = line.split('[')
        p = head.split('-')
        self.checksum = tail.strip(']')
        self.name = '-'.join(p[:-1])
        self.id = int(p[-1])
    
    @property 
    def isReal(self) -> bool:
        freq = defaultdict(int)
        for x in self.name:
            if x == '-': continue 
            freq[x] += 1
        freq = sorted((-v,k) for k,v in freq.items())
        if len(freq) < 5: 
            return False 
        top5 = ''.join(x for _,x in freq[:5])
        return top5 == self.checksum
    
    def decrypt(self) -> str: 
        msg = list(self.name)
        for _ in range(self.id):
            msg = [rotate(letter) for letter in msg]
        return ''.join(msg)

def data(full: bool) -> list[Room]:
    return [Room(line) for line in readLines(16, 4, full)]

def part1():
    full = True 
    total = 0 
    for room in data(full):
        if room.isReal:
            total += room.id 
    print(total) 

def part2():
    full = True 
    goal = 'northpole-object-storage'
    for room in data(full):
        if room.decrypt() == goal:
            print(room.id)
            break

def rotate(letter: str) -> str:
    if letter == 'z':
        return 'a'
    elif letter == '-':
        return '-'
    return chr(ord(letter)+1)

if __name__ == '__main__':
    do(part1)
    do(part2)

'''
Part1:
- Loop through each room, sum up roomID of valid rooms 
- Count frequency of letters in name (except -)
- Get top5 most frequent letters and check if same as checksum 

Part2:
- Loop through each room and decrypt room name to find 'northpole-object-storage'
- Repeat roomID times: rotate each letter in the name 
- Rotate letter: next letter with wraparound (Z => A); dont translate '-'
'''