# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge_two_lists(self, list1: ListNode, list2: ListNode) -> ListNode:
        node = ListNode()
        current = node

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2.next = list2
            
            current = current.next

        if list1:
            current.next = list1
        if list2:
            current.next = list2

        return node.next

     


solution = Solution()
solution.merge_two_lists([1, 2, 4], [1, 3, 4])