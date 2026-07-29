class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = res = 0
        for i in range (len(nums)):
            if (nums[i]==0):
                res = max (res, c)
                c = 0
            else:
                c +=1
        return max(res, c)