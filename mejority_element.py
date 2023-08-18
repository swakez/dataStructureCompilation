"""class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_dict = {}
        for num in nums:
            if num in num_dict:
                num_dict[num] = num_dict[num] + 1
            else:
                num_dict[num] = 1
        for count in num_dict:
            if num_dict[count] > (len(nums)/2):
                return num
"""

