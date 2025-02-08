import math
from typing import Optional


class PrimeGenerator:
    _is_crossed: list[Optional[bool]]
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
        cls._is_crossed = [False] * (max_value + 1)
        for i in range(2, len(cls._is_crossed)):
            cls._is_crossed[i] = False

    @classmethod
    def _cross_out_multiples(cls) -> None:
        max_prime_factor = cls._calc_max_prime_factor()
        for i in range(2, max_prime_factor):
            if cls._not_crossed(i):
                cls._cross_out_multiples_of(i)
    
    @classmethod
    def _calc_max_prime_factor(cls) -> int:
        max_prime_factor: float = math.sqrt(len(cls._is_crossed)) + 1
        return int(max_prime_factor)

    @classmethod
    def _cross_out_multiples_of(cls, i: int) -> None:
        for multiple in range(2*i, len(cls._is_crossed), i):
            cls._is_crossed[multiple] = True

    @classmethod
    def _not_crossed(cls, i: int) -> bool:
        return cls._is_crossed[i] == False
    

    @classmethod
    def _put_uncrossed_integers_into_result(cls) -> None:
        cls._result = [0] * cls._number_of_uncrossed_integers()
        j = 0
        for i in range(2, len(cls._is_crossed)):
            if cls._not_crossed(i):
                cls._result[j] = i
                j += 1

    @classmethod
    def _number_of_uncrossed_integers(cls) -> int:
        count: int = 0
        for i in range(2, len(cls._is_crossed)):
            if cls._not_crossed(i):
                count += 1
        
        return count