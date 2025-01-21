class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        current = result
        carry = 0

        while l1 or l2 or carry:
            # Get values from the lists or 0 if list is empty
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            # Calculate sum and new carry
            total = x + y + carry
            carry = total // 10
            digit = total % 10

            # Create new node with the digit
            current.next = ListNode(digit)
            current = current.next

            # Move to next nodes if they exist
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return result.next