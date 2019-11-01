import math


class Solution:
    def countPrimes1(self, n: int):
        primes = []
        for i in range(2, n):
            j = 0
            is_prime = True
            for p in primes:
                if p * p > i:
                    break
                if i % p == 0:
                    is_prime = False
            if is_prime:
                primes.append(i)
        return len(primes)

    def countPrimes(self, n: int):
        is_prime = [True] * (n - 2)
        for i in range(int(math.sqrt(n)) - 1):
            v = i + 2
            if is_prime[i]:
                for p in range(v * 2, n, v):
                    is_prime[p - 2] = False
        return len([p for p in is_prime if p])


print(Solution().countPrimes(10))
print(Solution().countPrimes(3))

print(Solution().countPrimes(499979))
print(Solution().countPrimes1(499979))