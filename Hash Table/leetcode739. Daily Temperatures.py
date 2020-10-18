class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        l =  len(T)
        res = [0] * l
        s = []
        for i, v in enumerate(T):
            while s and s[-1][0] < v:
                tmp_v = s.pop()[1]
                res[tmp_v] = i - tmp_v 
            s.append((v, i))
        return res