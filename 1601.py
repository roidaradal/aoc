# Advent of Code 2016 Day 01
# John Roy Daradal 

from lib import * 

def data(full: bool) -> list[list[strInt]]:
    def convert(line: str) -> list[strInt]:
        moves: list[strInt] = []
        for x in line.split(','):
            x = x.strip() 
            moves.append((x[0], int(x[1:])))
        return moves 
    return [convert(line) for line in readLines(16, 1, full)]

def part1():
    full = True 
    for moves in data(full):
        curr = (0, 0)
        d: delta|None = None 
        for turn, steps in moves:
            if d is None:
                d = L if turn == 'L' else R 
            elif turn == 'L':
                d = leftOf[d]
            elif turn == 'R':
                d = rightOf[d]
            for _ in range(steps):
                curr = move(curr, d)
        print(sum(abs(x) for x in curr))

def part2():
    full = True 
    for moves in data(full):
        end = walk(moves)
        print(sum(abs(x) for x in end))

def walk(moves: list[strInt]) -> coords:
    curr = (0, 0)
    d: delta|None = None 
    visited = set()
    for turn, steps in moves:
        if d is None: 
            d = L if turn == 'L' else R 
        elif turn == 'L':
            d = leftOf[d]
        elif turn == 'R':
            d = rightOf[d]
        for _ in range(steps):
            curr = move(curr, d)
            if curr in visited:
                # first coords that's visited twice
                return curr 
            visited.add(curr)


if __name__ == '__main__':
    do(part1)
    do(part2)

'''
Part1:
- Initialize: coords = (0,0), delta = first turn
- Process (turn,steps) sequentially 
- Apply turn left or turn right to current delta
- Repeatedly move coords by numSteps
- Manhattan distance: sum of abs(row) + abs(col) of final coords

Part2:
- Same walk as in Part 1 
- Keep set of visited coords 
- After each move, check if resulting coords is already visited
- Return the first coords that is already visited
'''