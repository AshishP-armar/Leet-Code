class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        answer = []
        
        def sort_criteria(item):
            
            return (-item[1], -item[0])
        
        for i in range(n - k + 1):
            subarray = nums[i:i + k]
            
            freq = Counter(subarray)
            
            top_elements = sorted(freq.items(), key=sort_criteria)
            
            x_elements = top_elements[:x]
            
            x_sum = sum(num * count for num, count in x_elements)
            
            answer.append(x_sum)
        
        return answer
