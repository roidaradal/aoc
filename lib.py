import time, hashlib
from collections.abc import Callable
from collections import defaultdict

coords = tuple[int,int]
delta  = tuple[int,int]

def do(fn: Callable):
    start = time.time()
    fn()
    duration = time.time() - start 
    print('\nTime: %.2fs' % duration)
    print('-----' * 5)

def readLines(year: int, day: int, full: bool, strip: bool = True) -> list[str]:
    if full:
        path = 'data/%d/%.2d.txt' % (year, day)
    else:
        path = 'test/%d%.2d.txt' % (year, day)
    f = open(path, 'r')
    lines = [x.strip() if strip else x for x in f.readlines()]
    f.close()
    return lines

def move(c: coords, d: delta) -> coords:
    row,col = c 
    dy,dx = d 
    return (row+dy, col+dx)

def md5Hash(word: str) -> str:
    return hashlib.md5(word.encode('utf-8')).hexdigest()
