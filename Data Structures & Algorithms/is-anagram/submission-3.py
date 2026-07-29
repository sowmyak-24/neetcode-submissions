class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        scount = defaultdict(int)
        tcount = defaultdict(int)
        for i in s:
            scount[i] += 1
        for i in t:
            tcount[i] += 1
        for j in scount:
            if scount[j] != tcount[j]:
                result = False
                break
            result = True
        return result

