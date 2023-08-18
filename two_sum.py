# Attempt 1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #i_1,i_2 = -1
        len_num = len(nums)
        for i in range(len_num):
            for j in range(i+1,len_num):
                if nums[i]+nums[j] == target:
                    return [i,j]