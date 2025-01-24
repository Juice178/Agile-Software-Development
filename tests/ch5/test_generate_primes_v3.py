from src.ch5.generate_primes_v3 import PrimeGenerator


class TestGeneratePrimes:
    name: str
    @classmethod
    def setup_class(cls, name: str = "TestGeneratePrimes") -> None:
        cls.name = name

    def test_null_array(self) -> None:
        null_array: list[int] = PrimeGenerator.generate_primes(0)
        assert len(null_array) == 0, f"Array size is {len(null_array)}"

    def test_min_array(self) -> None:
        min_array: list[int] = PrimeGenerator.generate_primes(2)
        assert len(min_array) == 1, f"Array size is {len(min_array)}"
        assert min_array[0] == 2, f"First element of array is {min_array[0]}"

    def test_three_array(self) -> None:
        three_array: list[int] = PrimeGenerator.generate_primes(3)
        assert len(three_array) == 2, f"Array size is {len(three_array)}"
        assert three_array[0] == 2, f"First element of array is {three_array[0]}"
        assert three_array[1] == 3, f"Second element of array is {three_array[0]}"

    def test_cent_array(self) -> None:
        cent_array: list[int] = PrimeGenerator.generate_primes(100)
        assert len(cent_array) == 25, f"Array size is {len(cent_array)}"
        assert cent_array[24] == 97
