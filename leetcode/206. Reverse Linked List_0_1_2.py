"""
    역순 연결 리스트
    2. 반복 구조로 뒤집기
"""
from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, prev = head, None
        while node:
            # print("bf prev={0}".format(prev))
            # print("bf node={0}".format(node))

            # print("af prev={0}".format(prev))
            # print("af node={0}".format(node))

            save_next, node.next = node.next, prev
            prev, node = node, save_next

        return prev
