import sys

sys.path.append('../Lessons/lesson4')

import parentheses


class TestCheckBrackets:
    error_message = "В выражении не согласованы скобки"
    true_message = "Скобки расставлены правильно"

    def test_different_numbers_of_opening_and_closing_brakets(self):
        assert parentheses.check_parentheses('(()[]') == self.error_message

    def test_misplaced_brakets_string_with_intersection(self):
        assert parentheses.check_parentheses('(([)])') == self.error_message

    def test_misplaced_brakets_string_with_trailing_brakets_first(self):
        assert parentheses.check_parentheses('([]][)') == self.error_message

    def test_empty_string(self):
        assert parentheses.check_parentheses('') == self.true_message

    def test_right_brakets_string_with_nested_brakets(self):
        assert parentheses.check_parentheses('{}[{({()})}]') == self.true_message