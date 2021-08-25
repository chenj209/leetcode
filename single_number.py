# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/

# Give a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# you must implement a solution witha linear runtime complixty and use only constant extra space
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for num in nums:
            a ^= num
        return a

if __name__ == "__main__":
    sol = Solution()
    assert(sol.singleNumber([2,2,1]) == 1)
    assert(sol.singleNumber([4,1,2,1,2]) == 4)
    assert(sol.singleNumber([1]) == 1)
