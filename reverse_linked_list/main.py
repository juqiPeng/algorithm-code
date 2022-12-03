

class ListNode:
    def __init__(self, x, next: 'ListNode' = None):
        self.val = x
        self.next = next

    def __str__(self) -> str:
        return f'Node({self.val})'

    def __repr__(self) -> str:
        return self.__str__()


class Solution:

    def reverseList(self, head: ListNode) -> ListNode:
        node = head
        stack = []
        while node:
            stack.append(node)
            node = node.next
        if not stack:
            return
        reversed_head = current_node = stack.pop()
        while stack:
            tmp_node = stack.pop()
            current_node.next = tmp_node
            current_node = tmp_node
        current_node.next = None
        return reversed_head


# ----------------------------
# 双指针版本
class SolutionV2:

    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        pre = None

        while cur:
            _next = cur.next
            cur.next = pre
            pre = cur
            cur = _next
        return pre


# ----------------------------
# 递归版本
class SolutionV3:

    def reverseList(self, head: ListNode) -> ListNode:

        def recur(cur, pre):
            if not cur:
                return pre
            _next = recur(cur.next, cur)
            cur.next = pre
            return _next
        return recur(head, None)


def show_link_list(head: ListNode):
    node = head
    r = []
    while node:
        r.append(str(node.val))
        node = node.next
    str_link = '->'.join(r)
    print(str_link)


if __name__ == '__main__':
    n5 = ListNode(5, None)
    n4 = ListNode(4, n5)
    n3 = ListNode(3, n4)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)
    show_link_list(n1)
    reversed_head = SolutionV3().reverseList(n1)    
    show_link_list(reversed_head)
