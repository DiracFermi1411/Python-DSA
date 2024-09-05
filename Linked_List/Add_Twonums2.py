# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):

        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)

        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        while l1 or l2:

            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        if carry > 0:
            current.next = ListNode(carry)
        
        # while dummy_head:
        while dummy_head:
            print(dummy_head.val, end=" -> " if dummy_head.next else "\n")
            dummy_head = dummy_head.next

        # dummy_head.next = self.reverseList(dummy_head.next)

        return dummy_head
    
    def reverseList(self, head):

        prev = None
        current = head

        while current:

            head_next = current.next
            current.next = prev
            prev = current
            current = head_next
        
        return prev
    
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
l1 = sol.create_linked_list([7, 2, 4, 3])
l2 = sol.create_linked_list([5, 6, 4])
result = sol.addTwoNumbers(l1, l2)
sol.print_linked_list(result)  # Expected output: [7, 8, 0, 7]





