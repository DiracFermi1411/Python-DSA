# # Definition for singly-linked list.

# ## Iterative appraoch ##
# class ListNode:
#     def __init__(self, val=5, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reverseList(self, head):
#         prev = None
#         current = head

#         while current:
#             next_node = current.next
#             current.next = prev
#             prev = current
#             current = next_node
#         return prev
    
## Recursive approach ##

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):

        if not head or not head.next:
            return head
        
        new_head = self.reverseList(head.next)

        head.next.next = head
        head.next = None

        return new_head

# Example usage:
# Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode)))))

solution = Solution()
reversed_head = solution.reverseList(head)

# Printing reversed list
while reversed_head:
    print(reversed_head.val, end=" -> " if reversed_head.next else "\n")
    reversed_head = reversed_head.next
