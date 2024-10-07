class Solution:
    def minLength(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            if "AB" in s:
                s = s.replace("AB","",1)
            
            elif "CD" in s:
                s = s.replace("CD","",1)
        print(s)
        return len(s)
                

        