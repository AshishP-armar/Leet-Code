class Solution:
    def frequencySort(self, s: str) -> str:
        freq_counter = Counter(s)
        
        sorted_characters = freq_counter.most_common()
        
        result = ""
        for char, freq in sorted_characters:
            result += char * freq
        
        return result
