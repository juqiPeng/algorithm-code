# 从尾到头打印链表

## 要求

输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

## 样例

```shell
输入：head = [1,3,2]
输出：[2,3,1]
```
## 思路

通常打印是一个只读操作，那么在打印不修改内容的情况下，也就是不去改变链表的结构，从尾到头打印链表每个节点的值，也就是说我肯定是要循环遍历链表，但遍历的顺序是从头到尾，而输出却是从尾到头，也就是第一个遍历的节点最后输出，最后一个遍历的节点最先输出

方法一：使用栈结构，第一次遍历的链表的值，将值压入栈中，再将栈中所有节点元素的值输出
