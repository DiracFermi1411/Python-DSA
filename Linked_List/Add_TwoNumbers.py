# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):

        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        while l1 or l2 or carry:

            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            l1 = l1.next
            l2 = l2.next

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

# Test case
sol = Solution()
l1 = sol.create_linked_list(arr = [2, 4, 3])
l2 = sol.create_linked_list(arr = [5, 6, 4])
result = sol.addTwoNumbers(l1, l2)
sol.print_linked_list(result) 

            
