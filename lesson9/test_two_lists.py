import sys

sys.path.append('../Lessons/lesson4')

import two_lists


class TestElementsMatch():
    def test_matching_empty_lists(self):
        assert two_lists.elements_match([], []) == True

    def test_matching_different_count_elements_lists(self):
        assert two_lists.elements_match([1], [1, 2]) == False

    def test_matching_equal_count_elements_lists_with_different_items(self):
        assert two_lists.elements_match([1, 4, 3], [1, 2, 3]) == False

    def test_matching_equal_sets_lists_with_different_items_count(self):
        assert two_lists.elements_match([1, 3, 3], [1, 3]) == True

    def test_matching_equal_sets_lists_with_equal_items_count(self):
        assert two_lists.elements_match([1, 2, 3], [1, 3, 2]) == True