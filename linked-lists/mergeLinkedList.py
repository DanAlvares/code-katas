# https://leetcode.com/problems/merge-two-sorted-lists/description/

#  Approach:
# 1. Create a new ListNode object and a tail object.
# 2. While both the input lists are not empty, compare the values of the two lists.
# 3. If the value of the first list is less than the value of the second list, then append the first list to the tail.
# 4. If the value of the first list is greater than the value of the second list, then append the second list to the tail.
# 5. Move the tail to the next node.
# 6. If the first list is not empty, then append the first list to the tail.
# 7. If the second list is not empty, then append the second list to the tail.
# 8. Return the next node of the output list.


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        output = ListNode()
        tail = output

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return output.next
