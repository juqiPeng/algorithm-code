import typing as t


# -----------------------------------------------------------------------------
# 版本一，写得非常不优雅 !!! 时间、内存占用都不尽如人意
# Time: 416ms   Memory: 19.2 MB
# 总结：最后一行使用函数调用，又重新跑了一次判断，开销自然增加，开启优化

class CQueueV1:

    def __init__(self) -> None:
        self._in_stack = []
        self._out_stack = []

    def appendTail(self, value: t.Any) -> None:
        self._in_stack.append(value)

    def deleteHead(self) -> t.Any:

        if self._out_stack:
            return self._out_stack.pop()

        if not self._in_stack:
            return -1

        while self._in_stack:
            self._out_stack.append(self._in_stack.pop())

        return self.deleteHead()


# -----------------------------------------------------------------------------
# 版本2，优化最后一行调用函数后
# Time: 356ms   Memory: 19 MB
# 时间得到了一定的优化


class CQueue:

    def __init__(self) -> None:
        self._in_stack = []
        self._out_stack = []

    def appendTail(self, value: t.Any) -> None:
        self._in_stack.append(value)

    def deleteHead(self) -> t.Any:

        if self._out_stack:
            return self._out_stack.pop()

        if not self._in_stack:
            return -1

        while self._in_stack:
            self._out_stack.append(self._in_stack.pop())

        return self._out_stack.pop()


if __name__ == '__main__':

    queue = CQueue()
    queue.appendTail(3)
    val1 = queue.deleteHead()
    print(val1)
    val2 = queue.deleteHead()
    print(val2)
    val3 = queue.deleteHead()
    print(val3)
