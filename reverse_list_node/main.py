from typing import List


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


# -----------------------------------------------------------------------------
# 版本一，使用辅助栈收集结果
# Time: 32ms   Memory: 16.5 MB
class Solution:

    def reversePrint(self, head: ListNode) -> List[int]:
        node = head
        stack = []
        while node:
            stack.append(node)
            node = node.next
        r = []
        while stack:
            r.append(stack.pop().val)
        return r


# -----------------------------------------------------------------------------
# 版本二，直接调用反转列表API快速实现
# Time: 44ms   Memory: 16.6 MB
# 效率反而还下降了
class SolutionV2:

    def reversePrint(self, head: ListNode) -> List[int]:
        node = head
        r = []
        while node:
            r.append(node.val)
            node = node.next
        return r[::-1]
