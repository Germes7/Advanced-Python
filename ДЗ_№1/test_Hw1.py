from hypothesis import given
import hypothesis.strategies as st
from Hw_1 import digit_sum

@given(st.integers())
def test_digit_sum_properties(number):

    result = digit_sum(number)
    assert result >= 0

    if 0 <= number <= 9:
        assert result == number