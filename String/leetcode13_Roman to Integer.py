class Solution:
    def romanToInt(self, s: str) -> int:
        prev_s, total = None, 0
        d = {"I": 1,
             "V":5,
             "X":10,
             "L":50,
             "C":100,
             "D":500,
             "M":1000}
        
        for e in s:
            total += d.get(e)
            if d.get(prev_s) is not None and d.get(prev_s) < d.get(e):
                total -= 2 * d.get(prev_s)
            prev_s = e
        return total