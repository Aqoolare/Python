import square_equation


class TestSolve:
    def test_with_not_null_real_args_with_real_roots(self):
        assert square_equation.solve(1, 2, 1) == (-1.0, -1.0)

    def test_with_real_args_roots_and_zero_c(self):
        assert square_equation.solve(1, 2, 0) == (-2.0, 0.0)

    def test_with_real_args_roots_and_zero_b(self):
        assert square_equation.solve(1, 0, -1) == (-1.0, 1.0)

    def test_with_real_args_roots_and_zero_a(self):
        assert square_equation.solve(0, 2, 4) == -2.0

    def test_with_zero_d(self):
        assert square_equation.solve(9, 6, 1) == (-0.33, -0.33)
    
    def test_with_real_args_and_complex_roots(self):
        assert square_equation.solve(9, 6, 1) == (-0.33, -0.33)

    def test_with_real_args_and_complex_roots(self):
        assert square_equation.solve(1, 0, 1) == (complex('-j'), complex('j'))

    def test_with_zero_a_b_and_not_zero_c(self):
        assert square_equation.solve(0, 0, 1) == None

    def test_with_zero_a_b_c(self):
        assert square_equation.solve(0, 0, 0) == 'inf'


    def test_with_wrong_args(self):
        assert square_equation.solve('a', '', 0) == 'wrong args'


