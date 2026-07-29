class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        tmp = []
        for i in range (len(nums)):
            if (nums[i] != val):
                tmp.append(nums[i])     
        for i in range (len(tmp)):
            nums[i] = tmp[i]

        return len(tmp)


