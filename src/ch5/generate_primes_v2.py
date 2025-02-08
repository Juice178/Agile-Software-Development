from math import sqrt, ceil
from typing import Optional


class PrimeGenerator:
    _s: int
    _f: list[bool]
    _primes: list[Optional[int]]

    @classmethod
    def generate_primes(cls, max_value: int) -> list[Optional[int]]:
        if max_value < 2:
            return []
        else:
            cls._initialize_sieve(max_value)
            cls._seive()
            cls._load_primes()
            return cls._primes
        
    @classmethod
    def _load_primes(cls) -> None:
        count: int = 0
        for i in range(cls._s):
            if cls._f[i]:
                count += 1
            
        cls._primes = [0] * count

        j = 0
        for i in range(cls._s):
            if cls._f[i]:
                cls._primes[j] = i
                j += 1
    
    @classmethod
    def _seive(cls) -> None:
        for i in range(2, ceil(sqrt(cls._s))+1):
            if cls._f[i]:
                for j in range(2*i, cls._s, i):
                    cls._f[j] = False

    @classmethod
    def _initialize_sieve(cls, max_value: int) -> None:
        cls._s = max_value + 1
        cls._f = [False] * cls._s

        for i in range(cls._s):
            cls._f[i] = True

        cls._f[0] = cls._f[1] = False
