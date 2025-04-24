# Advent of Code 2015 Day 03
# John Roy Daradal 

from lib import * 

T: dict[str,delta] = {
    '>' : (0,1),
    '<' : (0,-1),
    '^' : (1,0),
    'v' : (-1,0),
}

def data(full: bool) -> list[list[delta]]:
    def convert(line: str) -> list[delta]:
        return [T[x] for x in line]
    return [convert(line) for line in readLines(15, 3, full)]

def part1():
    full = True 
    for moves in data(full):
        curr = (0,0)
        visited = set([curr])
        for d in moves:
            curr = move(curr, d)
            visited.add(curr)
        print(len(visited))

def part2():
    full = True 
    for moves in data(full):
        santa, robo = (0,0), (0,0)
        visited = set([santa])
        for i in range(0, len(moves)-1, 2):
            santa = move(santa, moves[i])
            robo  = move(robo,  moves[i+1])
            visited.add(santa)
            visited.add(robo)
        print(len(visited))

if __name__ == '__main__':
    do(part1)
    do(part2)

'''
Data:
- Translate < left  (0,-1)
- Translate > right (0,1)
- Translate ^ up    (1,0)
- Translate v down  (-1,0)

Part1:
- Start at (0,0)
- Apply all deltas in succession to current coords
- Keep set of visited coords

Part2:
- Similar processing to Part 1
- Separate coords for santa and robo 
- Process moves in pairs: one for santa, one for robo
'''