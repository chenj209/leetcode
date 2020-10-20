# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # keep a advance flag, if current two nodes exceed 10, then advance flag will be set to True
        advance_flag = (l1.val + l2.val) >= 10
        cur_l1 = l1
        cur_l2 = l2
        while cur_l1 is not None or cur_l2 is not None:
            cur_l1_val = cur_l1.val if cur_l1 is not None else 0
            cur_l2_val = cur_l2.val if cur_l2 is not None else 0
            next_val = cur_l1_val + cur_l2_val + advance_flag
            next_output = ListNode(val=((next_val)%10))
            advance_flag = next_val >= 10
            cur_output.next = next_output
            cur_output = next_output

        return output
