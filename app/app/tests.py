"""
Sample tests
"""
from django.test import SimpleTestCase
from app import calc

class CalcTest(SimpleTestCase):
    """Test the calc module."""
    
    def test_add_numbers(self):
        """Test adding numbers."""
        res = calc.add(2,3)
        self.assertEqual(5, res)