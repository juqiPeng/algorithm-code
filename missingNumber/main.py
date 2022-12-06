import typing as t


# --------------------------------------------------------------------------------------------------------
# 一行代码解决，根据题目描述的，0～n-1内递增数据只有一个不再数组中，找出索引位置不等于数据值的那个元素，索引位就是缺失值，否则就是元素值最后一个值 + 1
class Solution:

    def missingNumber(self, nums: t.List[int]) -> int:
        return next((i for i, val in enumerate(nums) if val != i), nums[-1]+1)



# --------------------------------------------------------------------------------------------------------
# 运用数学思想：原数组的总和 - 当前数组的总和 = 缺失值
# 原数组的值可以看作是等差数列的和
# 但是这样两次遍历求和将会带来更大的开销
class Solution:

    def missingNumber(self, nums: t.List[int]) -> int:
        return sum(range(len(nums)+1)) - sum(nums)


# --------------------------------------------------------------------------------------------------------
# 使用二分查找，当中间值等于索引值，说明左侧的数据没有缺失，将查询窗口右移，否则说明左侧已经出现了缺失，就需要将窗口左移
# 
class Solution:

    def missingNumber(self, nums: t.List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == mid:
                l = mid + 1
            else:
                r = mid - 1
        return l 



if __name__ == '__main__':
    nums = [0, 1, 3]
    r = Solution().missingNumber(nums)
    print(r)
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 9]
    r = Solution().missingNumber(nums)
    print(r)
    nums = [0]
    r = Solution().missingNumber(nums)
    print(r)