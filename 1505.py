# Advent of Code 2015 Day 05
# John Roy Daradal 

from lib import * 

def data(full: bool) -> list[str]:
    return readLines(15, 5, full)

def part1():
    full = True 
    count = 0
    for word in data(full):
        if isNice(word):
            count += 1
    print(count)

def part2():
    full = True 
    count = 0 
    for word in data(full):
        if isNice2(word):
            count += 1 
    print(count)

invalid = ('ab','cd','pq','xy')
vowels = 'aeiou'

def isNice(word: str) -> bool:
    # Check if contains any of the invalid substrings
    if any(x in word for x in invalid): 
        return False 
    
    # Check if has letter that appears twice in a row (aa)
    hasRepeat = False 
    count = defaultdict(int)
    for i in range(len(word)-1):
        curr, next = word[i], word[i+1]
        count[curr] += 1
        if curr == next:
            hasRepeat = True
    count[next] += 1
    if not hasRepeat: 
        return False

    # Check if has at least 3 vowels
    numVowels = sum(count.get(v,0) for v in vowels)
    return numVowels >= 3

def isNice2(word: str) -> bool:
    wordLen = len(word)

    # Check if contains letter which repeats with one letter between them (e.g. axa)
    hasRepeat = False 
    for i in range(2, wordLen):
        if word[i] == word[i-2]:
            hasRepeat = True
            break 
    if not hasRepeat:
        return False 
    
    # Check if has pair of two letters that appears >= 2 with no overlap
    pairs = defaultdict(list)
    for i in range(wordLen-1):
        pair = word[i:i+2]
        pairs[pair].append(i)
    for pair,indexes in pairs.items():
        if len(indexes) >= 3:
            return True 
        elif len(indexes) ==2 and abs(indexes[0]-indexes[1]) >= 2:
            # if only two indexes, make sure has gap of at least 2
            return True    
    return False

if __name__ == '__main__':
    do(part1)
    do(part2)

'''
Part1:
- Check if word contains any of invalid substrings (ab, cd, pq, xy)
- Check if word has letter that appears twice in a row (e.g. aa, bb)
- Check if word has at least 3 vowels 

Part2:
- Check if contains letter which repeats with one letter between them
- Check if has pair of two letters that appears >= 2 with no overlap
    - Group the pairs' indexes 
    - If pair has at least 3 indexes, valid 
    - If pair only has 2 indexes, check that index difference is at least 2 (no overlap)
'''