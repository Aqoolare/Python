import sys

sys.path.append('../Lessons/lesson4')

import list_elements


class TestListElements:
    def test_empty_list(self):
        assert list_elements.select_elements([]) == []
    
    def test_repeating_elements_list(self):
        assert list_elements.select_elements([1, 1, 1]) == [1]

    def test_list_of_different_elements(self):
        assert list_elements.select_elements([1, 2, 3]) == [1, 2, 3]

    def test_list_with_repeating_and_different_elements(self):
        assert list_elements.select_elements([1, 1, 1, 2, 3, 3]) == [1, 2, 3]