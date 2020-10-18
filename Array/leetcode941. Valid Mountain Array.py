class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        arrLen = len(A)
        if arrLen <= 2: return False
        
        for i in range(1, arrLen):
            if A[i] > A[i+1]: break
            
            elif A[i] is A[i+1]: return False
        
        if i is 0: return False

        for j in range(i, arrLen):
            if A[j] < A[j+1]: return False
            
            elif A[j] is A[j+1]: return False
        return True
                