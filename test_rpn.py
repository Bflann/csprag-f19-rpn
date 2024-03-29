import unittest
import rpn
    
class TestBasics(unittest.TestCase):
    
    def test_add(self):
        result = rpn.calculate('1 1 +')
        self.assertEqual(2, result)
            
    def test_sub(self):
        result = rpn.calculate('5 3 -')
        self.assertEqual(2, result)
            
    def test_bad_input(self):
        with self.assertRaises(TypeError):
            rpn.calculate('1 2 3 +')

    def test_carrot(self):
        result = rpn.calculate('2 2 ^')
        self.assertEqual(4, result)
            
if __name__ == '__main__':
    test = TestBasics()
    test.test_add()
    test.test_bad_input()
    test.test_sub()
    test.test_carrot()
