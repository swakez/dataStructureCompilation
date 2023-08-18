class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        run_sum = []
        run_sum.append(nums[0])
        for i in range(1,len(nums)):
            run_sum.append(run_sum[i-1] + nums[i])
        return run_sum


# https://leetcode.com/problems/running-sum-of-1d-array/submissions/