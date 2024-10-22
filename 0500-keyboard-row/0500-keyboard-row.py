class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiopQWERTYUIOP")
        row2 = set("asdfghjklASDFGHJKL")
        row3 = set("ZXCVBNMzxcvbnm")    
        result = []
        for word in words:
            if word[0] in row1:
                for w in range(1,len(word)):
                    if word[w] not in row1:
                        break
                else:
                    result.append(word)
            elif word[0] in row2:
                for w in range(1,len(word)):
                    if word[w] not in row2:
                        break
                else:
                    result.append(word)
            else:
                for w in range(1,len(word)):
                    if word[w] not in row3:
                        break
                else:
                    result.append(word)
        return result

                    
