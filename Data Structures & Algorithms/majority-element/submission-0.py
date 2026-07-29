class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for val in nums:
            d[val] += 1
        for k in d:
            if (d[k] > (len(nums)) // 2):
                return k
         
 