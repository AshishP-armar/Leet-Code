class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        if len(hours)==2 and (hours[0] + hours[1])%24==0:
            return 1

        i = 0
        j= i+1
        count =0
        while i<(len(hours)-2):
            if j==len(hours):
                i+=1
                j=i+1
            if (hours[i] + hours[j])%24==0: 
                count +=1
            
            j+=1
        return count