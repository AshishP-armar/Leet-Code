class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        while len(word) < k:
            next_word = "".join(
                chr(((ord(c) - ord('a') + 1) % 26) + ord('a')) for c in word
            )
            word += next_word
        
        return word[k - 1]
