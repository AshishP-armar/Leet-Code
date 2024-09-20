# https://leetcode.com/problems/majority-element/description/

"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        temp = {}

        # making Dictnory for numbers count
        for num in nums:
            if num not in temp:
                temp[num]=1
            else:
                temp[num]+=1

        count = 0
        result = 0

        for key,value in temp.items():
            if value>count:
                result=key
                count=value

        return result