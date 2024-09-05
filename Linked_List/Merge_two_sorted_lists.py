# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):

        if not list1 and not list2:
            return list1
        
        dummy_head = ListNode(0)
        current = dummy_head
        
        while list1 and list2:

            if list1.val <= list2.val:
                current.next = ListNode(list1.val)
                if list1:list1 = list1.next
            else:
                current.next = ListNode(list2.val)
                if list2: list2 = list2.next
            
            current = current.next

        if list1:
            current.next = list1
        
        if list2:
            current.next = list2

        
        return dummy_head.next
    
    def create_linked_list(self, arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def print_linked_list(self, head):
        values = []
        while head:
            values.append(head.val)
            head = head.next
        print(values)


sol = Solution()
list1 = sol.create_linked_list([0])
list2 = sol.create_linked_list([])
result = sol.mergeTwoLists(list1, list2)
sol.print_linked_list(result)  # Expected output: [1,1,2,3,4,4]


