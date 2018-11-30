def getIntersectionNode(self, headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    d=dict()
    current_A=headA
    current_B=headB
    while current_A:
        d[current_A]=True
        current_A=current_A.next
    while current_B:
        if current_B in d:
            return current_B
        current_B=current_B.next
    return None
