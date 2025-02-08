from math import sqrt, ceil
from typing import Optional


class GeneratePrimes:
    @staticmethod
    def generate_primes(max_value: int) -> list[Optional[int]]:
        if max_value >= 2:
            s: int = max_value + 1
            f: bool = [False] * s
            i: int = 0

            for i in range(s):
                f[i] = True
            
            f[0] = f[1] = False

            j: int = 0
            for i in range(2, ceil(sqrt(s))+1):
                if f[i]:
                    for j in range(2*i, s, i):
                        f[j] = False

            count: int = 0
            for i in range(s):
                if f[i]:
                    count += 1
            
            primes: list[int] = [0] * count

            j = 0
            for i in range(0, s):
                if f[i]:
                    primes[j] = i
                    j += 1

            return primes
        else:
            return []


