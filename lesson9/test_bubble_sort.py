import sys

sys.path.append('../Lessons/lesson4')

import bubble_sort


class TestBubbleSort():
    def test_sorting_empty_list(self):
        l = []
        bubble_sort.bubble_sort(l)
        assert l == []

    def test_sorting_1_element_list(self):
        l = [1]
        bubble_sort.bubble_sort(l)
        assert l == [1]

    def test_sorting_sorted_list(self):
        l = [1, 2, 3, 4, 5]
        bubble_sort.bubble_sort(l)
        assert l == [1, 2, 3, 4, 5]

    def test_sorting_unsorted_list(self):
        l = [5, 2, 4, 1, 3]
        bubble_sort.bubble_sort(l)
        assert l == [1, 2, 3, 4, 5]

    def test_sorting_reverse_sorted_list(self):
        l = [5, 2, 4, 1, 3]
        bubble_sort.bubble_sort(l)
        assert l == [1, 2, 3, 4, 5]