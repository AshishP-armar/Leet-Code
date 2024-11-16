class Solution:
    def isValid(self, word: str) -> bool:
        if len(word)<3:
            return False
        vowel = set("aieouAEIOU")
        nums = set("1234567890")
        consonant = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
        temp = set()

        for char in word:
            if char not in vowel and char not in nums and char not in consonant:
                return False
            elif char in vowel:
                if "V" not in temp:
                    temp.add("V")
        
            elif char in consonant:
                if "C" not in temp:
                    temp.add("C")

        return len(temp)==2