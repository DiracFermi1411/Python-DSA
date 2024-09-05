class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        if not head or not head.next:
            return False
        
        slow = head
        fast = head

        while fast and fast.next:  # Ensure fast.next is not None
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False
    
    # Helper function to create a linked list with a cycle
    def createLinkedListWithCycle(self, values, pos):
        if not values:
            return None
        
        head = ListNode(values[0])
        current = head
        cycle_node = None
        
        if pos == 0:
            cycle_node = head
        
        for index in range(1, len(values)):
            current.next = ListNode(values[index])
            current = current.next
            if index == pos:
                cycle_node = current
        
        if cycle_node:
            current.next = cycle_node
        
        return head

    # Helper function to create a linked list without a cycle
    def createLinkedList(self, values):
        if not values:
            return None
        
        head = ListNode(values[0])
        current = head
        for value in values[1:]:
            current.next = ListNode(value)
            current = current.next
        
        return head

# Instantiate Solution to use its methods
solution = Solution()

# Test Case 1: Linked list with a cycle
values_with_cycle = [3, 2, 0, -4]
pos_with_cycle = 1
head_with_cycle = solution.createLinkedListWithCycle(values_with_cycle, pos_with_cycle)
print("Test Case 1 - Expected: True, Got:", solution.hasCycle(head_with_cycle))  # Output: True

# Test Case 2: Linked list without a cycle
values_without_cycle = [1, 2]
head_without_cycle = solution.createLinkedList(values_without_cycle)
print("Test Case 2 - Expected: False, Got:", solution.hasCycle(head_without_cycle))  # Output: False
