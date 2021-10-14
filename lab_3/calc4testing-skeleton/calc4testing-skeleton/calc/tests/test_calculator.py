from calc.calculator import calculator as c
import unittest

# TODO: Extend these unit tests for the calculator module!


class TestAdd(unittest.TestCase):
    def test_add_integers_positive(self):
        result = c.sum(1, 2)
        self.assertEqual(result, 3)

    def test_add_integers_negative(self):
        result = c.sum(-1, -2)
        self.assertEqual(result, -3)

    def test_add_integers_pos_neg(self):
        result = c.sum(1, -2)
        self.assertEqual(result, -1)

    def test_add_integers_neg_pos(self):
        result = c.sum(-1, 2)
        self.assertEqual(result, 1)

    def test_divide_integers_positive(self):
        result = c.divide(6, 3)
        self.assertEqual(result, 2)

    def test_divide_integers_positive2(self):
        result = c.divide(7, 3)
        self.assertEqual(result, 2)
        
    def test_divide_integrs_positive3(self):
        result = c.divide(2,10)
        self.assertEqual(result,0)

    def test_divide_integers_negative(self):
        result = c.divide(-6, -2)
        self.assertEqual(result, 3)

    def test_divide_integers_negative2(self):
        result = c.divide(-7, -2)
        self.assertEqual(result, 3)
        
    def test_divide_integers_negative3(self):
        result = c.divide(-2,-10)
        self.assertEqual(result,0)

    def test_divide_integers_pos_neg(self):
        result = c.divide(6, -2)
        self.assertEqual(result, -3)

    def test_divide_integers_pos_neg2(self):
        result = c.divide(9, -2)
        self.assertEqual(result, -4)

    def test_divide_integers_neg_pos(self):
        result = c.divide(-6, 2)
        self.assertEqual(result, -3)

    def test_divide_integers_neg_pos2(self):
        result = c.divide(-7, 2)
        self.assertEqual(result, -3)

    def test_divide_zero(self):
        result = c.divide(0, 2)
        self.assertEqual(result, 0)

    def test_divide_by_zero(self):
        self.assertRaises(ZeroDivisionError, c.divide, 6, 0)

    ######################################################################################################################à
    
    
    def test_multiply_integers_positive(self):
        result = c.multiply(6, 3)
        self.assertEqual(result, 18)

    def test_multiply_integers_positive2(self):
        result = c.multiply(7, 3)
        self.assertEqual(result, 21)
        
    def test_multiply_integrs_positive3(self):
        result = c.multiply(2,10)
        self.assertEqual(result,20)

    def test_multiply_integers_negative(self):
        result = c.multiply(-6, -2)
        self.assertEqual(result, 12)

    def test_multiply_integers_negative2(self):
        result = c.multiply(-7, -2)
        self.assertEqual(result, 14)
        
    def test_multiply_integers_negative3(self):
        result = c.multiply(-2,-10)
        self.assertEqual(result,20)

    def test_multiply_integers_pos_neg(self):
        result = c.multiply(6, -2)
        self.assertEqual(result, -12)

    def test_multiply_integers_pos_neg2(self):
        result = c.multiply(9, -2)
        self.assertEqual(result, -18)

    def test_multiply_integers_neg_pos(self):
        result = c.multiply(-6, 2)
        self.assertEqual(result, -12)

    def test_multiply_integers_neg_pos2(self):
        result = c.multiply(-7, 2)
        self.assertEqual(result, -14)

    def test_multiply_zero(self):
        result = c.multiply(0, 2)
        self.assertEqual(result, 0)
    
############################################################################

    def test_subtract_integers_positive(self):
        result = c.subtract(1, 2)
        self.assertEqual(result,-1)

    def test_subtract_integers_negative(self):
        result = c.subtract(-2,-5)
        self.assertEqual(result,3)

    def test_subtract_integers_pos_neg(self):
        result = c.subtract(1, -2)
        self.assertEqual(result, 3)

    def test_subtract_integers_neg_pos(self):
        result = c.subtract(-1, 2)
        self.assertEqual(result, -3)

    


if __name__ == "__main__":
    unittest.main()
