from typing import List

DEBUG = 1

def debug_print(s):
    if DEBUG:
        print(s)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashed_nums = {}
        for i, num in enumerate(nums):
            hashed_nums[num] = i
        for i, num in enumerate(nums):
            residual = target - num
            if residual in hashed_nums and hashed_nums[residual] != i:
                return [i, hashed_nums[residual]]
        return []

class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        debug_print(f"input nums: {nums}")
        sorted_lst = nums[:]
        sorted_lst.sort()
        debug_print(sorted_lst)
        left = 0
        right = len(sorted_lst) - 1
        current_sum = sorted_lst[left] + sorted_lst[right]
        debug_print(f"left: {left}, right: {right}, current_sum: {current_sum}")
        while (left < right) and current_sum != target:
            if current_sum > target:
                right -= 1
            elif current_sum < target:
                left += 1
            current_sum = sorted_lst[left] + sorted_lst[right]
            debug_print(f"left: {left}, right: {right}, current_sum: {current_sum}")
        if left >= right:
            return []
        first_num = sorted_lst[left]
        second_num = sorted_lst[right]
        results = []
        idx = 0
        while nums[idx] != first_num:
            idx += 1
        results.append(idx)
        idx = 0
        while idx == results[0] or nums[idx] != second_num:
            idx += 1
        results.append(idx)

        return results


def main(l1, l2):
    solution = Solution()
    out = solution.twoSum(l1, l2)
    print(f"results:{out}")

if __name__ == "__main__":
    main([2,7,11,15], 9)
    main([3,2,4], 6)
    main([3,3], 6)


