
# ------------------------------------------------------
# 借用一个顺序的哈希表做缓存
class Solution:
    def firstUniqChar(self, s: str) -> str:
        if not s:
            return ' '
        cache = {}
        for _ in s:
            cache[_] = _ not in cache
        return next((k for k, v in cache.items() if v), ' ')


if __name__ == "__main__":
    s = "abaccdeff"
    r = Solution().firstUniqChar(s)
    print(r)

    s = ""
    r = Solution().firstUniqChar(s)
    print(r)
