class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        k = [0,0]
        for i in range (len(nums)):
            for j in range (i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    k[0] = i
                    k[1] = j
                    break
        return k
                