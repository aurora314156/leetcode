class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        i, j = 0, 1
        while i < len(target) and j <=n:
            res.append("Push")
            if target[i] == j:
                i += 1
            else:
                res.append("Pop")
            j+=1
        return res