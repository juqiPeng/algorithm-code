
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = x
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return
        cache = {}
        curr = head
        while curr:
            # 建立旧节点到新节点的映射关系
            cache[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            new_curr = cache[curr]
            new_curr.next = cache.get(curr.next)
            new_curr.random = cache.get(curr.random)
            curr = curr.next
        return cache[head]


class SolutionV2:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: 
            return
        cur = head
        # 1. 复制各节点，并构建拼接链表
        while cur:
            tmp = Node(cur.val)
            tmp.next = cur.next
            cur.next = tmp
            cur = tmp.next
        # 2. 构建各新节点的 random 指向
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        # 3. 拆分两链表
        cur = res = head.next
        pre = head
        while cur.next:
            pre.next = pre.next.next
            cur.next = cur.next.next
            pre = pre.next
            cur = cur.next
        pre.next = None  # 单独处理原链表尾节点
        return res      # 返回新链表头节点
