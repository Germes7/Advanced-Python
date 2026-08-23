from hypothesis import given
import hypothesis.strategies as st
from Hw_1 import digit_sum, is_prime

# 1.
@given(st.integers())
def test_digit_sum_properties(number):

    result = digit_sum(number)
    assert result >= 0

    if 0 <= number <= 9:
        assert result == number

# 2.
@given(st.integers())
def test_is_prime_properties(number):

    if number < 2:
        assert is_prime(number) is False
        return

    result = is_prime(number)

    if number > 2 and number % 2 == 0:
        assert result is False

    if number in [2, 3, 5, 7, 11]:
        assert result is True