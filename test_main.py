# this file was written by me using advice from Ask mode😎

from main import bubble_sort, parse_input_array
import pytest


array_base_cases = [
    ([5, 2, 8, 6, 6], [2, 5, 6, 6, 8]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([3, 1, 3, 1, 2], [1, 1, 2, 3, 3]),
]

array_edge_cases = [
    ([], []),
    ([1], [1]),
    ([2, 1], [1, 2]),
]

parsing_base_cases = [
    ("1,2,3", [1, 2, 3]),
    (" 1 , 2 , 3 ", [1, 2, 3]),
    ("1,2,3,", [1, 2, 3]),
]

parsing_edge_cases = ["", " ", "???", ",,,"]


@pytest.mark.parametrize(("case", "answer"), array_base_cases)
def test_array_base_cases(case, answer):
    assert bubble_sort(case) == answer


@pytest.mark.parametrize(("case", "answer"), array_edge_cases)
def test_single_and_small_arrays(case, answer):
    assert bubble_sort(case) == answer


@pytest.mark.parametrize(("case", "answer"), parsing_base_cases)
def test_parsing_base_cases(case, answer):
    assert parse_input_array(case) == answer


@pytest.mark.parametrize("case", parsing_edge_cases)
def test_parsing_edge_cases(case):
    with pytest.raises(ValueError):
        parse_input_array(case)
