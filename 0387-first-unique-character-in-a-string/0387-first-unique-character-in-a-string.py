class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}

        for char in s:
            if char not in count:
                count[char] = 1
            else:
                count[char]+=1
        temp = ""
        for key,value in count.items():
            if value==1:
                temp = key
                break

        if temp!="":
            return s.index(temp)

        return -1
        