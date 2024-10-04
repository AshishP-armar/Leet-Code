class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill)==2:
            return skill[0]*skill[1]

        skill.sort()
        i=1
        j = len(skill)-2
        temp = []
        while i<j:
            if skill[i]+ skill[j]!=skill[0] + skill[-1]:
                return -1
            else:
                temp.append([skill[i],skill[j]])
                i+=1
                j-=1
        
        temp.append([skill[0],skill[-1]])
        result = 0
        
        for arr in temp:
            result += arr[0]*arr[1]

        return result

        
        