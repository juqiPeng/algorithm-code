# -----------------------------------------------------------------------------
# 版本一，时间不够快
# Time: 60ms   Memory: 18.6 MB


class MinStack:

    def __init__(self):
        self.data, self._min = [], []

    def push(self, x: int) -> None:
        self.data.append(x)
        if not self._min or self._min[-1] >= x:
            self._min.append(x)

    def pop(self) -> None:
        if self.data.pop() == self._min[-1]:
            self._min.pop()

    def top(self) -> int:
        return self.data[-1]

    def min(self) -> int:
        return self._min[-1]


# -----------------------------------------------------------------------------
# 版本二，不使用pop(), 而是直接 del 删除栈顶元素，时间有显著提升
# Time: 48ms   Memory: 18.7 MB


class MinStack:

    def __init__(self):
        self.data, self._min = [], []

    def push(self, x: int) -> None:
        self.data.append(x)
        if not self._min or self._min[-1] >= x:
            self._min.append(x)

    def pop(self) -> None:
        if self.data[-1] == self._min[-1]:
            del self._min[-1]
        del self.data[-1]
        
    def top(self) -> int:
        return self.data[-1]

    def min(self) -> int:
        return self._min[-1]
