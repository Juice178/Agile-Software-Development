from math import sqrt, ceil
from typing import Optional


class PrimeGenerator:
    _f: list[bool]
    _result: list[Optional[int]]

    @classmethod
    def generate_primes(cls, max_value: int) -> list[Optional[int]]:
        if max_value < 2:
            return []
        else:
            cls._initialize_array_of_integers(max_value)
            cls._cross_out_multiples()
            cls._put_uncrossed_integers_into_result()
            return cls._result

    @classmethod
    def _initialize_array_of_integers(cls, max_value: int) -> None:
        cls._f = [False] * (max_value + 1)
        cls._f[0] = cls._f[1] = False
        for i in range(2, len(cls._f)):
            cls._f[i] = True

    @classmethod
    def _cross_out_multiples(cls) -> None:
        for i in range(2, ceil(sqrt(len(cls._f)))+1):
            if cls._f[i]:
                for j in range(2*i, len(cls._f), i):
                    cls._f[j] = False

    @classmethod
    def _put_uncrossed_integers_into_result(cls) -> None:
        count: int = 0
        for i in range(len(cls._f)):
            if cls._f[i]:
                count += 1
            
        cls._result = [0] * count

        j = 0
        for i in range(len(cls._f)):
            if cls._f[i]:
                cls._result[j] = i
                j += 1
    