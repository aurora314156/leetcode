class Solution:
    def minOperations(self, logs: List[str]) -> int:
        s = []
        for l in logs:
            if l[:2] == "..":
                if len(s) == 0: continue
                s.pop()
            elif l[:2] != "./":
                s.append(1)
        return len(s)