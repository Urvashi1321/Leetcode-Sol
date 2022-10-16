class Solution:
    def minDifficulty(self, A: List[int], d: int) -> int:
        n = len(A)
        if n < d:
            return -1
        
        dp = [[0] + [float('inf')] * n for _ in range(d + 1)]
        
        for day in range(1, d + 1):
            stack = []
            for j in range(day, n + 1):
    			# schedule j at the dayth days
                dp[day][j] = dp[day - 1][j - 1] + A[j - 1] 
                while stack and A[stack[-1] - 1] <= A[j - 1]:
                    i = stack.pop()
					# find i such that A[i] <= A[j], then schedule i at the same day as j
                    dp[day][j] = min(dp[day][j], dp[day][i] - A[i - 1] + A[j - 1])
                if stack:
				    # j might not be the max, schedule j at the same day as the max
                    dp[day][j] = min(dp[day][j], dp[day][stack[-1]])
                stack.append(j)
        return dp[-1][-1]