class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(' ', '%20')


class Solution:
    def replaceSpace(self, s: str) -> str:
        return ''.join('%20' if i == ' ' else i for i in s)
