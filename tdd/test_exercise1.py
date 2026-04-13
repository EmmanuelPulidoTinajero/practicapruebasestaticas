import unittest
import exercise1 from test_exercise1.py 
class TestExercise1(unittest.TestCase):
    def Test_Exercise1_Multiples _Of_Three (self):
        result = exercise1(15)
        result = result % 3
        self.assertEqual(result, "Fizz")
    
    def Test_Exercise1_Multiples _Of_Five (self):
        result = exercise1(10)
        result = result % 5
        self.assertEqual(result, "Buzz")
    
    def Test_Exercise1_Multiples _Of_Three_And_Five (self):
        result = exercise1(30)
        result = result % 3 and result % 5
        self.assertEqual(result, "FizzBuzz")