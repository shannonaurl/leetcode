# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        list_size = 0 
        count_ptr = head 
        while count_ptr: 
            list_size += 1 
            count_ptr = count_ptr.next 


        count_so_far = 0 
        tmp = head 
        prev = None 

        if n == 0: 
            return head 

        if n == list_size: 
            head = head.next
            return head  

        while count_so_far < (list_size - n): 
            count_so_far += 1 
            prev = tmp 
            tmp = tmp.next
        
        prev.next = tmp.next

        return head 

        