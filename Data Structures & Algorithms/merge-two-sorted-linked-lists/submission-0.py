# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        current1 = list1
        current2 = list2
        while current1 and current2:
            if current1.val <= current2.val:
                tail.next = current1
                tail = current1
                current1 = current1.next
            elif current2.val <= current1.val:
                tail.next = current2
                tail = current2
                current2 = current2.next
        else:
            if current1 == None and current2 != None:
                tail.next = current2
            elif current2 == None and current1 != None:
                tail.next = current1
            
        return dummy.next
        