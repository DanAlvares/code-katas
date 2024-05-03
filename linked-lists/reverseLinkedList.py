# https://leetcode.com/problems/reverse-linked-list/description/

class IterativeSolution(object):
    def reverseList(self, head):
        prev, curr = None, head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev


class RecursiveSolution(object):
    def reverseList(self, head):
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        
        return newHead