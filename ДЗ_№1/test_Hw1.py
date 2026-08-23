from hypothesis import given
import hypothesis.strategies as st
from Hw_1 import digit_sum, is_prime, triangle_area, count_words

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

# 3.
@given(
    st.floats(min_value=0.1, max_value=10000.0),
    st.floats(min_value=0.1, max_value=10000.0)
)
def test_triangle_area_properties(base, height):

    result = triangle_area(base, height)

    assert result > 0

    if base == 2.0 and height == 2.0:
        assert result == 2.0

# 4.
@given(st.text(), st.integers(min_value=1, max_value=100))
def test_count_words_properties(text, min_length):
    result = count_words(text, min_length)

    assert result >= 0
    assert result <= len(text.split())