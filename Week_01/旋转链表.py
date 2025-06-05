# 给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 排除空值
        if head==None:
            return head

        # 求链表长度
        l = 1
        cur_head = head
        while cur_head.next:
            l+=1
            print(f"l: {l}")
            cur_head=cur_head.next

        # 排除链表长度1
        if l==1:
            return head

        # 排除旋转步数实际为0
        k = k%l
        if k==0:
            return head

        # 连成环
        cur_head.next = head


        #切割
        a = l-k
        while a>0:
            cur_head = cur_head.next
            a -= 1
        ret = cur_head.next
        cur_head.next = None
        return ret

a = [1,3,2]
a.sort(reverse=True)

