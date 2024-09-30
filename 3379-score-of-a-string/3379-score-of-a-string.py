class Solution:
    def scoreOfString(self, s: str) -> int:
        result = []
        for i in range(1,len(s)):
            result.append(abs(ord(s[i-1]) - ord(s[i])))
        

        return sum(result)