import sys

sys.path.append('../Lessons/lesson4')

import opz


class TestOPZ:
    wrong_format = '\nНеверный формат выражения'
    wrong_brackets = '\nВ выражении не согласованы скобки'

    def test_count_from_opz(self):
        assert opz.count_from_opz(['3', '(-)', '4', '2', '*', '1', '5', '-', 
        '2', '^', '/', '+']) == '-2.50'

    def test_wrong_format_expression(self):
        assert opz.count_expression('1+a') == self.wrong_format

    def test_wrong_brackets(self):
        assert opz.count_expression('(1+1))') == self.wrong_brackets

    def test_expression_with_one_op(self):
        assert opz.count_expression('(1+1)(())') == '2.00'

    def test_expression_with_sum_in_pow_with_negative_args(self):
        assert opz.count_expression('(-5)^(-5+6)') == '-5.00'

    def test_expression_with_two_different_ops_with_brackets(self):
        assert opz.count_expression('(5+10)*(13-3)') == '150.00'

    def test_expression_with_negative_ground_of_pow(self):
        assert opz.count_expression('(-10)^2') == '100.00'

    def test_expression_with_three_ops_and_brackets(self):
        assert opz.count_expression('10+(30-25)*2') == '20.00'

    def test_expression_with_pow_of_negative_numbers(self):
        assert opz.count_expression('(-2)^(-1)') == '-0.50'

    def test_expression_with_three_ops_in_exponent_and_negative_ground(self):
        assert opz.count_expression('(-5)^((1+2)*(3-3))') == '1.00'

    def test_complex_expression_with_all_ops(self):
        assert opz.count_expression('-((1+2)^2+2*10/2)^((1+2)*(3-2))') == '-6859.00'