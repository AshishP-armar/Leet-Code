class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp = sorted(tuple(arr))
        result = []
        rank_dict = {}
        rank = 1
        for i in range(len(temp)):
            if temp[i] not in rank_dict:
                rank_dict[temp[i]]=rank
                rank+=1
       
        for num in arr:
            result.append(rank_dict[num])

        return result
        