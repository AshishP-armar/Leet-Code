class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = set(["a","A","e","E","i","I","O","o","u","U"])
        temp = self.s_to_list(s)
        i = 0
        j = len(s) - 1

        while i<j:
            if temp[i] in vowel and temp[j] in vowel:
                temp[i],temp[j] = temp[j],temp[i]
                i+=1
                j-=1

            elif temp[i] not in vowel:
                i+=1
            elif temp[j] not in vowel:
                j-=1
        result =""
        for i in temp:
            result +=i
        return result
        

    def s_to_list(self,s):
        temp = []
        for i in s:
            temp.append(i)
        return temp

