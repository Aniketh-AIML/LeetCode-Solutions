class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:

        n = len(nums)
        # values =[]

        # for i in range(n):
        #     for j in range(n):
        #         if j - i >= k:
        #             values.append(nums[i] + nums[j])

        # if values:
        #     return max(values)

        # return -1

        best = nums[0]
        ans = -1
        
        for j in range(k,n):
            best = max(best, nums[j-k])
            ans = max(ans, best + nums[j])
        
        return ans
            
        