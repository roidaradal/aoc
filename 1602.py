# Advent of Code 2016 Day 02
# John Roy Daradal 

from lib import * 

T: dict[str,delta] = {'U': U, 'D': D, 'L': L, 'R': R}

def data(full: bool) -> list[str]:
    return readLines(16, 2, full)

def part1():
    full = True 
    pad = ['123','456','789']
    curr, bounds = (1,1), (3,3)
    code = []
    for moves in data(full):
        for m in moves:
            nxt = move(curr, T[m])
            if insideBounds(nxt, bounds):
                curr = nxt 
        row,col = curr 
        code.append(pad[row][col])
    print(''.join(code))

def part2():
    full = True 
    pad = ['00100','02340','56789','0ABC0','00D00']
    curr, bounds = (2,0), (5,5)
    code = []
    for moves in data(full):
        for m in moves:
            nxt = move(curr, T[m])
            if insideDiamond(nxt, bounds, pad):
                curr = nxt 
        row,col = curr 
        code.append(pad[row][col])
    print(''.join(code))

def insideDiamond(c: coords, bounds: dims2, pad: list[str]) -> bool:
    row, col = c 
    return insideBounds(c, bounds) and pad[row][col] != '0'


if __name__ == '__main__':
    do(part1)
    do(part2)

'''
Part1:
- Start at (1,1) = "5"
- Process moves UDLR: moving coords by delta
- Ignore if move makes coords go out of bounds
- After each line's moves, store current coords location in pad 
- Combine all code results

Part2:
- Similar processing to Part 1 
- Start at (2,0) = "5" position in diamond pad 
- insideDiamond: check if insideBounds and coords' mapped character in pad is not '0'
'''