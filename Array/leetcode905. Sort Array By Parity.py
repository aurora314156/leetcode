class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        if not A or len(A) == 1: return A
        i, j  = 0, len(A)-1
        while i < j: 
            while i < j and A[i] % 2 == 0:
                i += 1
            while j > -1 and A[j] % 2 != 0: 
                j -= 1
            if i > j: break
            A[i], A[j] = A[j], A[i]
        return A