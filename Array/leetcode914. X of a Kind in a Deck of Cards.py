class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) < 2: return False
        d = collections.Counter(deck)
        m = min(d.values())
        def check(i):
            for n in d:
                if d[n] % i != 0:
                    return False
            return True
        for i in range(2, m+1):
            if check(i):
                return True
        return False