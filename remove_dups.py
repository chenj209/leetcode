from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # strategy 1:
            # first scan replaces all dups with empty sign
            # second scan keeps a list of indices for empty spaces encountered so far
            # exchange each unique elem with the first empty spaces avail

        # first scan
        prev_elem = None
        for i, elem in enumerate(nums):
            if elem == prev_elem:
                nums[i] = "_"
            else:
                prev_elem = elem


        # second scan
        emp_idx = []
        counter = 0
        for i, elem in enumerate(nums):
            if elem == "_":
                emp_idx.append(i)
            else:
                counter += 1
                if len(emp_idx):
                    nums[emp_idx.pop(0)] = elem
                    nums[i] = "_"
                    emp_idx.append(i)
        return counter


if __name__ == "__main__":
    sol = Solution()
    nums = [1,1,2]
    print(sol.removeDuplicates(nums))
    print(nums)
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(sol.removeDuplicates(nums))
    print(nums)


