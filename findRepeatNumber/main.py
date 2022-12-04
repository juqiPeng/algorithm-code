import typing as t

# --------------------------------------------------
# 蛮力法
class Solution:
    def findRepeatNumber(self, nums: t.List[int]) -> int:
        cache = []
        for num in nums:
            if num in cache:
                return num
            cache.append(num)


# --------------------------------------------------
# 蛮力法 2.0, 使用哈希结构存储缓存，优化查询性能
class Solution:
    def findRepeatNumber(self, nums: t.List[int]) -> int:
        cache = set()
        for num in nums:
            if num in cache:
                return num
            cache.add(num)


# --------------------------------------------------
# 先排序，再遍历列表，然后判断当前元素与下一个元素是否相同
class Solution:
    def findRepeatNumber(self, nums: t.List[int]) -> int:
        nums.sort()
        lenght = len(nums)
        for idx in range(1, lenght+1):
            if nums[idx-1] == nums[idx]:
                return nums[idx]


# --------------------------------------------------
# 将值存储在对应的索引位
class Solution:
    def findRepeatNumber(self, nums: t.List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == i:
                i += 1
                continue
            if nums[nums[i]] == nums[i]: return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return -1
