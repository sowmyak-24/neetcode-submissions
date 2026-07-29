class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        LR, RR = 0, len(matrix) - 1 
        LC, RC = 0, len(matrix[0]) - 1
        while (LR <= RR):
            Rmid = (LR + RR) // 2
            if (target > matrix[Rmid][0]):
                if (target <= matrix[Rmid][RC]):
                    break
                LR = Rmid + 1
            elif (target < matrix[Rmid][0]):
                if (target >= matrix[Rmid][RC]):
                    break
                RR = Rmid - 1
            else:
                return True
        
        while (LC <= RC):
            Cmid = (LC + RC) // 2
            if (target > matrix[Rmid][Cmid]):
                LC = Cmid + 1
            elif (target < matrix[Rmid][Cmid]):
                RC = Cmid - 1
            else:
                return True
        return False
