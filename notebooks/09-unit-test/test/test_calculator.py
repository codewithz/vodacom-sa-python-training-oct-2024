import calculator as sut 
# sut -- system under test
import unittest

class TestCalculator(unittest.TestCase):

    def test_add(self):
        #Arrange/Given
        a=2
        b=3
        # Act /When
        result =sut.add(a,b)
        # Assert / Then
        # self.assertEqual(actual,expected)
        self.assertEqual(result,5)

    
    def test_subtract(self):
        #Arrange/Given
        a=5
        b=3
        # Act /When
        result =sut.subtract(a,b)
        # Assert / Then
        # self.assertEqual(actual,expected)
        self.assertEqual(result,2)

    def test_multiply(self):
        #Arrange/Given
        a=20
        b=3
        # Act /When
        result =sut.multiply(a,b)
        # Assert / Then
        # self.assertEqual(actual,expected)
        self.assertEqual(result,60)
    def test_divide(self):
        #Arrange/Given
        a=15
        b=5
        # Act /When
        result =sut.divide(a,b)
        # Assert / Then
        # self.assertEqual(actual,expected)
        self.assertEqual(result,3)

        with self.assertRaises(ValueError):
            sut.divide(10,0)


# ---------------------End of class-------------------------------------------

if __name__ == '__main__':
    unittest.main()
    