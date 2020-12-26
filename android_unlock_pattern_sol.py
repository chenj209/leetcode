class Solution:
    def __init__(self):
        self.used = {i: False for i in range(9)}
        self.counts = [0, 0, 0]
        self.paths = []

    def numberOfPatterns(self, m, n):
        res = 0
        for l in range(m, n+1):
            paths = ['']
            n, paths = self.calcPatterns(-1, l, paths)
            res += n
            self.paths += paths
            for i in range(9):
                self.used[i] = False
        self.paths.sort()
        print(self.paths)
        with open('expected.txt', 'w') as f:
            for path in self.paths:
                f.write(path)
                f.write('\n')
        return res

    def isValid(self, index, last):
        if (self.used[index]):
            return False
        # first digit of the pattern
        if (last == -1):
            return True
        # knight moves or adjacent cells (in a row or in a column)
        if ((index + last) % 2 == 1):
            return True
        # indexes are at both end of the diagonals for example 0,0, and 8,8
        mid = (index + last)/2
        if (mid == 4):
            return self.used[mid]
        # adjacent cells on diagonal  - for example 0,0 and 1,0 or 2,0 and //1,1
        if ((index%3 != last%3) and (index//3 != last//3)):
            return True
        # all other cells which are not adjacent
        return self.used[mid]

    def calcPatterns(self, last, l, paths):
        all_paths = []
        if (l == 0):
            return 1, paths
        sum = 0
        for i in range(9):
            if self.isValid(i, last):
                self.used[i] = True
                new_paths = []
                for j in range(len(paths)):
                    new_paths.append(paths[j] + f'{i+1}')
                n, new_paths = self.calcPatterns(i, l - 1, new_paths)
                sum += n
                all_paths += new_paths
                self.used[i] = False
        return sum, all_paths

if __name__ == '__main__':
    sol = Solution()
    print(sol.numberOfPatterns(1, 5))