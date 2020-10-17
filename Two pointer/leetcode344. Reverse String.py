class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s)-1
        for i in range(l//2+1):
            tmp = s[i]
            s[i] = s[l-i]
            s[l-i] = tmp