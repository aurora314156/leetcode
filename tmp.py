"""
Des: 350. Intersection of Two Arrays II
Algo: Binary search
"""
class Solution:
    def intersect(self, nums1 = list(), nums2 = list()):
        res, d = list(), dict()
        if len(nums1) > len(nums2):    
            for n in nums1:
                d[n] = d.get(n, 0) + 1
            for n in nums2:
                if d.get(n, 0) != 0:
                    d[n] = d.get(n, 0) - 1
                    res.append(n)
        else:
            for n in nums2:
                d[n] = d.get(n, 0) + 1
            for n in nums1:
                if d.get(n, 0) != 0:
                    d[n] = d.get(n, 0) - 1
                    res.append(n)      
        return res
            
            
            

a1, a2 = [4,9,5], [9,4,9,8,4]
res = Solution().intersect(a1, a2)
print(res)