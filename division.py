import unittest

def divide(a, b):
    """Divides a by b.

    Args:
        a (float): Numerator.
        b (float): Denominator.

    Returns:
        float: a divided by b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

# Unit Tests
class TestDivision(unittest.TestCase):
    def test_divide_positive_numbers(self):
        self.assertEqual(divide(10, 2), 5.0)

    def test_divide_negative_numbers(self):
        self.assertEqual(divide(-6, 3), -2.0)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == "__main__":
    unittest.main()
