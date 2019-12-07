"""
Des: Partition Labels
Algo: Greedy
"""
class Solution:
    def partitionLabels(self, S):
        Dict, string_len, res = dict(), len(S), []
        start, end = 0, 0
        for i in range(string_len):
            Dict[S[i]] = i
        for i in range(string_len):
            print("Current ind: {}.".format(i))
            print("End: {}, Word: {}, WordIndexOnString: {}.".format(end, S[i], Dict[S[i]]))
            end = max(end, Dict[S[i]])
            if i == end:
                print("Put {} into result.".format(i - start + 1))
                print("Start: {}".format(i+1))
                res.append(i - start + 1)
                start = i + 1
        return res

