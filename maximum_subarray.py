# https://leetcode.com/problems/maximum-subarray/
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # M[i] = the maximun sum ending at inex i
        # M[i] = max(M[i-1] + nums[i], nums[i])
        M = [0] * len(nums)
        M[0] = nums[0]
        for i in range(1,len(M)):
            M[i] = max([M[i-1]+nums[i], nums[i]])
        print(M)
        return max(M)

def main(lst):
    solution = Solution()
    print(f"Max subarray sum is {solution.maxSubArray(lst)}")

if __name__ == "__main__":
    main([1,2,-3,-4,2,7,-2, 3])

