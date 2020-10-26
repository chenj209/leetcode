# https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # M[i, j] = if the string starts at i and ends at j is palindromic/non-palindromic
        # M[i, j] = M[i] == M[j] and M[i+1, j-1]
        M = [[False for i in range(len(s))] for j in range(len(s))]
        max_len = -1
        max_str = ''
        for d in range(0, len(s)):
            for i in range(len(s) - d):
                j = i + d
                M[i][j] = (s[i] == s[j]) and (M[i+1][j-1] if (j-i+1) > 2 else True)
                if M[i][j] and (j - i + 1) > max_len:
                    max_len = j - i + 1
                    max_str = s[i:j+1]
        for m in M:
            print(m)
        return max_str

def main(s):
    solution = Solution()
    print(f"Longest palindrome is {solution.longestPalindrome(s)}")

if __name__ == "__main__":
    main("babad")
    main("cbbd")
    main("a")
    main("ac")
