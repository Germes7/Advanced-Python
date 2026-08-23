from hypothesis import given
import hypothesis.strategies as st
from Hw_1 import (digit_sum, is_prime, triangle_area, count_words, arithmetic_mean, count_by_sign,
                  replace_negatives, without_duplicates)

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

# 5.
@given(st.lists(st.floats(min_value=-1000.0, max_value=1000.0), min_size=1, max_size=50))
def test_arithmetic_mean_same_numbers(lst):

    single_num = lst[0]
    identical_list = [single_num] * len(lst)
    result = arithmetic_mean(*identical_list)


    assert abs(result - single_num) < 1e-9

def test_arithmetic_mean_empty():

    assert arithmetic_mean() is None

# 6.
@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=0, max_size=100))
def test_count_by_sign_properties(lst):

    result = count_by_sign(*lst)

    assert isinstance(result, list)
    assert len(result) == 3
    assert sum(result) == len(lst)
    assert result[0] >= 0
    assert result[1] >= 0
    assert result[2] >= 0

# 7.
@given(st.lists(st.integers(), min_size=0, max_size=100))
def test_replace_negatives_properties(lst):

    original_lst = lst.copy()
    replace_negatives(lst)

    assert len(lst) == len(original_lst)

    for i, num in enumerate(lst):

        assert num >= 0
        if original_lst[i] >= 0:
            assert num == original_lst[i]
        else:
            assert num == 0

# 8.
@given(st.lists(st.integers(), min_size=0, max_size=100))
def test_without_duplicates_properties(lst):

    original_lst = lst.copy()
    result = without_duplicates(lst)

    assert len(result) == len(set(result))
    assert set(result) == set(original_lst)
    assert lst == original_lst