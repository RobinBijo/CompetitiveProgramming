'''
Time Complexity O(n log n log n
'''

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        sieve = [True] * n
        sieve[0] = sieve[1] = False  # 0 and 1 are not prime
        for i in range(2, int(n ** 0.5) + 1):
            if sieve[i]:
                for j in range(i * i, n, i):
                    sieve[j] = False
        return sum(sieve)

