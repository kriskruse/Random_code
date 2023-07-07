class Solution(object):

    def solve(self, a, k, c):
        i = 0
        j = 0
        cnt = 0
        n = len(a)
        ans = 0

        while (j < n):
            if a[j] == c:
                cnt += 1
            while i < n and cnt > k:
                if a[i] == c:
                    cnt -= 1
                i += 1
            ans = max(j - i + 1, ans)
            j += 1

        return ans

    def maxConsecutiveAnswers(self, answerKey, k):
        """
        :type answerKey: str
        :type k: int
        :rtype: int
        """
        return max(self.solve(answerKey, k, 'T'), self.solve(answerKey, k, 'F'))
