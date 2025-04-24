# Advent of Code 2015 Day 02
# John Roy Daradal 

from lib import * 

int3 = tuple[int,int,int]

def data(full: bool) -> list[int3]:
    def convert(line: str) -> int3:
        return tuple(int(x) for x in line.split('x'))
    return [convert(line) for line in readLines(15, 2, full)]

def part1():
    full = True 
    total = 0 
    for l,w,h in data(full):
        lw, wh, lh = l*w, w*h, l*h 
        total += (2*lw) + (2*wh) + (2*lh) + min(lw,wh,lh)
    print(total)

def part2():
    full = True 
    total = 0 
    for dims in data(full):
        d1, d2, d3 = sorted(dims)
        total += (2 * (d1+d2)) + (d1*d2*d3)
    print(total)


if __name__ == '__main__':
    do(part1)
    do(part2)

'''
Part1:
- Sum up values computed with formula:
- 2*lw + 2*wh + 2*lh + min(lw,wh,lh)

Part2:
- Sort ascending the dimensions 
- Compute smallest face perimeter: 2 * (d1+d2)
- Add volume: d1*d2*d3
'''