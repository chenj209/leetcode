# https://leetcode.com/problems/add-two-numbers
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # keep a advance flag, if current two nodes exceed 10, then advance flag will be set to True
        cur_l1 = l1
        cur_l2 = l2
        output = None
        cur_out = None
        advance_val = 0
        while cur_l1 is not None or cur_l2 is not None:
            cur_l1_val = cur_l1.val if cur_l1 is not None else 0
            cur_l2_val = cur_l2.val if cur_l2 is not None else 0
            next_val = cur_l1_val + cur_l2_val + advance_val
            if cur_out is None:
                output = ListNode(val=next_val%10)
                cur_out = output
            else:
                cur_out.next = ListNode(val=next_val%10)
                cur_out = cur_out.next
            advance_val = int(next_val >= 10)
            if cur_l1 is not None:
                cur_l1 = cur_l1.next
            if cur_l2 is not None:
                cur_l2 = cur_l2.next
        if advance_val != 0:
            cur_out.next = ListNode(val=advance_val)
        return output

def init_list(lst):
    l = ListNode(lst[0])
    cur_l = l
    for num in lst[1:]:
        cur_l.next = ListNode(num)
        cur_l = cur_l.next
    return l

def main(l1, l2):
    l1 = init_list(l1)
    l2 = init_list(l2)
    solution = Solution()
    out = solution.addTwoNumbers(l1, l2)
    while out is not None:
        print(out.val)
        out = out.next

if __name__ == "__main__":
    main([2,4,3], [5,6,4])


