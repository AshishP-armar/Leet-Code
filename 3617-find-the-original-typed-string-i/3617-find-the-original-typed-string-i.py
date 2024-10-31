class Solution:
    def possibleStringCount(self, word: str) -> int:
        groups = []
        i = 0

        while i < len(word):
            j = i
            while j < len(word) and word[j] == word[i]:
                j += 1
            groups.append(j - i)  
            i = j

        result = 1

        for group_len in groups:
            if group_len > 1:
                result += group_len - 1  

        return result
