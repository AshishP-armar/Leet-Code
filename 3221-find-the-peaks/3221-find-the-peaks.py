class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        i = 1
        result = []
        while i<len(mountain)-1:
            if mountain[i-1]<mountain[i] and mountain[i]>mountain[i+1]:
                result.append(i)
            i+=1



        return result
        