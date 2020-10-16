class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B): return False
        
        sign, count = [], 0
        for i in range(len(A)):
            if A[i] != B[i]:
                sign.append(i)
                count += 1
        d = {}
        if count == 0:
            for a in A:
                # a already in A which means a appear twice in A
                if d.get(a):
                    return True
                else:
                    d[a] = True
        if count != 2:
            return False
        
        return A[sign[0]] == B[sign[1]] and A[sign[1]] == B[sign[0]]
    
    