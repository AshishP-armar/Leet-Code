class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        word_Set = set(word)
        temp = set()
        count = 0
        for i in word:
            if i.isupper():
                continue
            elif i.capitalize() in word_Set and i not in temp:
                temp.add(i)
                count+=1

        return count