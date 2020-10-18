"""
Des: majority number
Algo: boyer-moore voting algorithm
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n1, c1 = None, 0
        n2, c2 = None, 0
        for e in nums:
            if e == n1:
                c1 += 1
            elif e == n2:
                c2 += 1
            elif c1 == 0:
                n1, c1 = e, 1
            elif c2 == 0:
                n2, c2 = e, 1
            else:
                c1 -= 1
                c2 -= 1
        
        c1, c2 = 0, 0
        for e in nums:
            if e == n1:
                c1 += 1
            if e == n2:
                c2 += 1
        res = []
        if c1 > len(nums)/3:
            res.append(n1)
        if c2 > len(nums)/3:
            res.append(n2)
        return res
