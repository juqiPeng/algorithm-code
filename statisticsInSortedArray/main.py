import typing as t

# --------------------------------------------------------------------------------------------------------
# 这是所有人都能想到的一种解决方法：二分法找到target对应的index，如果找到则循环往左找左边界，循环往右找右边界，没找到则返回0。
# 并不优雅
class Solution:

    def search(self, nums: t.List[int], target: int) -> int:
        if not nums:
            return 0
        left = 0
        right = len(nums) - 1
        mid = None
        count = 0
        while left <= right:
            mid = (left+right) // 2
            mid_value = nums[mid]
            if mid_value == target:
                count += 1
                break
            if target > mid_value:
                left = mid + 1
            else:
                right = mid - 1

        flag_left = flag_right = 1 if count else False

        while flag_left and mid-flag_left >= 0:
            if nums[mid-flag_left] == target:
                count += 1
                flag_left += 1
                continue
            break

        while flag_right and mid + flag_right < len(nums):
            if nums[mid+flag_right] == target:
                count += 1
                flag_right += 1
                continue
            break

        return count


# --------------------------------------------------------------------------------------------------------
# 版本二：我们陷入了一种思维的泥潭，想着既然是求元素的数量，那么总想以统计的方法来求解
# 其实，我们可以找出分别找出左右边界，然后用(右边界 - 左边界 - 1) 就可以得到元素的数量
# 因此我们可以对左右两半边分别求解，因为相同的元素一定会被分到左右两边去的
class Solution:

    def search(self, nums: t.List[int], target: int) -> int:
        # 先搜索右边界 right
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            # 当目标值在当前位置的右边，我们需要收缩左侧的指针，让我们的查询窗口在当前位置的右边进行搜索
            if nums[m] <= target:
                i = m + 1
            else:
                j = m - 1
        right = i
        # 若数组中无 target ，则提前返回
        if j >= 0 and nums[j] != target:
            return 0
        # 搜索左边界 left
        i = 0
        while i <= j:
            m = (i + j) // 2
            if nums[m] < target:
                i = m + 1
            else:
                j = m - 1
        left = j
        return right - left - 1


if __name__ == "__main__":
    nums = [5, 7, 7, 8, 8, 10]
    r = Solution().search(nums, 8)
    print(r)

    nums = [2, 2]
    r = Solution().search(nums, 3)
    print(r)
