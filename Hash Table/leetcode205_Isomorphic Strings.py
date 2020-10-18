class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return [len(set(s)),len(set(t))] == 2 * [len(set(zip(s,t)))]