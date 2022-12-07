from typing import List


# --------------------------------------------------------
# 话不多少，先来一波蛮力法压压惊
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        return next((numbers[i] for i in range(1, len(numbers)) if numbers[i - 1] > numbers[i]), numbers[0])


# --------------------------------------------------------
# 遇到排序数组，我就上二分查找，就是干
# 在这个场景下面，由于左侧是升序的数组，右侧不是，只需要找到左侧升序的数组边界值即可
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        l, r = 0, len(numbers) - 1

        while l < r:
            mid = (l+r) // 2

            # 中间值比最右侧的值大，右侧区间内一定发生了旋转，否则一定会是右侧的值大
            if numbers[mid] > numbers[r]:
                l = mid + 1
            
            # 如果中间值比最右侧的值小，说明右侧区间一直保持递增，因此左侧区间内一定发生了旋转
            if numbers[mid] < numbers[r]:
                r = mid
            
            # 如果相等的话，是无法判断旋转值在何处，只能逐渐收缩
            else:
                return min(numbers[l:r])

        return numbers[l]


if __name__ == "__main__":
    # numbers = [3, 4, 5, 1, 2]
    # r = Solution().minArray(numbers)
    # print(r)
    numbers = [3, 1, 1, 1, 1]
    r = Solution().minArray(numbers)
    print(r)
