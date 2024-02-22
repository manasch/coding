import aocd
import heapq
import json
import math
import re

from collections import defaultdict, deque

class Solution:
    def __init__(self):
        with open("input.txt", encoding="utf-8") as f:
            self.input = f.read().splitlines()
            self.partOne = None
            self.partTwo = None

    def parse(self):
        self.input = [[ch for ch in row] for row in self.input]

    def solveOne(self):
        dish = [[ch for ch in row] for row in self.input]
        
        for j in range(len(dish[0])):
            count = 0
            for i in range(len(dish) - 1, -1, -1):
                if dish[i][j] == 'O':
                    count += 1
                    dish[i][j] = '.'
                elif dish[i][j] == '#':
                    for k in range(count):
                        dish[i + k + 1][j] = 'O'
                    count = 0
            if count > 0:
                for k in range(count):
                    dish[i + k][j] = 'O'

        res = 0
        for r, row in enumerate(dish):
            res += (len(dish) - r) * row.count('O')
        self.partOne = res
        
        # r1, r2 = [], []
        # for row, row2 in zip(self.input, dish):
        #     r1.append("".join(row))
        #     r2.append("".join(row2))
        # # print("\n".join(r1))
        # print()
        # print("\n".join(r2))      

    def solveTwo(self):
        pass

    def solve(self):
        self.parse()
        self.solveOne()
        self.solveTwo()

    def answer(self):
        print("Part One:", self.partOne)
        print("Part Two:", self.partTwo)

def main():
    solution = Solution()
    solution.solve()
    solution.answer()

if __name__ == "__main__":
    main()