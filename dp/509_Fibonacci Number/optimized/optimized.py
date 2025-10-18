class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        prev1 = 1
        prev2 = 0
        for i in range(2,n+1):
            curr = prev1+prev2
            prev2 = prev1
            prev1 = curr
        return prev1