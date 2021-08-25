# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/

from typing import List

DEBUG = 1
class Solution1:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ori_lst = nums[:]
        for i in range(len(nums)):
            nums[i] = ori_lst[(i-k) % len(nums)]
        if DEBUG:
            print(f"ori list: {ori_lst}")
            print(f"mod list: {nums}")

def single_shift_right(nums: List[int]) -> None:
    last_num = nums[-1]
    # nums[-1] = nums[-2]
    for i in range(len(nums)):
        ori_num = nums[i]
        nums[i] = last_num
        last_num = ori_num

class Solution2:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            single_shift_right(nums)

class Solution3:
    def rotate(self, nums: List[int], k: int) -> None:
        mod_k = k % len(nums)
        if mod_k == 0:
            return
        last_k = nums[-mod_k:]
        for i in range(0,len(nums),mod_k):
            ori_k = nums[i:i+mod_k]
            nums[i:min(i+mod_k,len(nums))] = last_k[:min(len(nums)-i,mod_k)]
            last_k = ori_k

def reverse_array(lst, start, end):
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1

class Solution4:
    def rotate(self, nums: List[int], k: int) -> None:
        if DEBUG:
            print(f"nums:{nums}, k:{k}")
        reverse_array(nums, 0, len(nums)-1)
        if DEBUG:
            print(f"reversed nums:{nums}")
        reverse_array(nums, 0, k-1)
        if DEBUG:
            print(f"reversed first k nums:{nums}")
        reverse_array(nums, k, len(nums)-1)
        if DEBUG:
            print(f"reversed rest nums:{nums}")

class Solution5:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        replace number in place
        """
        n = len(nums)
        start = 0
        cur_index = 0
        start = cur_index
        to_swap_val = nums[cur_index]
        count = 0
        while count < n:
            while True:
                swap_index = (cur_index + k) % n
                print(f"cur_index:{cur_index}, to_swap_val:{to_swap_val}, swap_index:{swap_index}")
                temp = nums[swap_index]
                nums[swap_index] = to_swap_val
                cur_index = swap_index
                to_swap_val = temp
                print(f"nums:{nums}")
                count += 1
                if swap_index == start or count >= n:
                    if DEBUG:
                        print(f"Cycle detected at index {swap_index}")
                    start += 1
                    to_swap_val = nums[start]
                    cur_index = start
                    break




if __name__ == "__main__":
    sol =  Solution6()
    lst1 = [1,2,3,4,5,6,7]
    sol.rotate(lst1, 3)
    print(lst1)
    assert(lst1 == [5,6,7,1,2,3,4])
    lst2 = [-1,-100,3,99]
    sol.rotate(lst2, 2)
    print(lst2)
    assert(lst2 == [3,99,-1,-100])
