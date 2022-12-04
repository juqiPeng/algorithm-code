class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]


class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        after = before = ''
        for idx, char in enumerate(s):
            if idx < n:
                after += char
                continue
            before += char
        
        return f'{before}{after}'


if __name__ == "__main__":
    print(Solution().reverseLeftWords("abcdefg", 2))