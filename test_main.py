import pytest
from main import bubble_sort


class TestBubbleSort:
    """Test suite for bubble_sort function."""

    def test_basic_unsorted_array(self):
        """Test sorting a basic unsorted array."""
        result = bubble_sort([5, 2, 8, 6, 6])
        assert result == [
            2,
            5,
            6,
            6,
            8,
        ], "Basic array should be sorted in ascending order"

    def test_already_sorted_array(self):
        """Test that an already sorted array remains sorted."""
        result = bubble_sort([1, 2, 3, 4, 5])
        assert result == [1, 2, 3, 4, 5], "Already sorted array should remain unchanged"

    def test_reverse_sorted_array(self):
        """Test sorting a reverse-sorted array."""
        result = bubble_sort([5, 4, 3, 2, 1])
        assert result == [
            1,
            2,
            3,
            4,
            5,
        ], "Reverse sorted array should be sorted in ascending order"

    def test_array_with_duplicates(self):
        """Test sorting an array with duplicate values."""
        result = bubble_sort([3, 1, 3, 1, 2])
        assert result == [
            1,
            1,
            2,
            3,
            3,
        ], "Array with duplicates should be sorted correctly"

    def test_single_and_small_arrays(self):
        """Test edge cases: empty and single-element arrays."""
        assert bubble_sort([]) == [], "Empty array should return empty"
        assert bubble_sort([5]) == [5], "Single-element array should return itself"
        assert bubble_sort([2, 1]) == [1, 2], "Two-element array should be sorted"
