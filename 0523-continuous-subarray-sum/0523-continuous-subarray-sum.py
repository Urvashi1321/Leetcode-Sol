class Solution:
     def checkSubarraySum(self, A, k):
        seen, cur = {0: -1}, 0
        for i, a in enumerate(A):
            cur = (cur + a) % abs(k) if k else cur + a
            if i - seen.setdefault(cur, i) > 1: return True
        return False
