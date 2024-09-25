# https://leetcode.com/problems/combination-sum-ii/description/
"""

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
"""

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start: int, target: int, path: List[int]):
            if target == 0:
                result.append(path)
                return
            for i in range(start, len(candidates)):
               
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                
                backtrack(i + 1, target - candidates[i], path + [candidates[i]])

        result = []
        candidates.sort()  
        backtrack(0, target, [])
        return result
