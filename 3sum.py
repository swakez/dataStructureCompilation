class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # print(num_dict)
        nums.sort()
        res = []
        n = len(nums)
        i = 0
        while (i < n):
            t = 0 - nums[i]
            s = i + 1
            e = n - 1
            while (s < e):
                if nums[s] + nums[e] == t:
                    res.append([nums[i], nums[s], nums[e]])
                    while ((s < e) and (nums[s + 1] == nums[s])):
                        s += 1
                    while ((e > s) and (nums[e - 1] == nums[e])):
                        e -= 1
                    s += 1
                    e -= 1
                elif nums[s] + nums[e] < t:
                    s += 1
                else:
                    e -= 1
            while ((i < (n - 1)) and nums[i + 1] == nums[i]):
                i += 1
            i += 1
        return res

