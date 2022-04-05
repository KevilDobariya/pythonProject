import unittest
from unit_test_example import unit_test_examples

class MyTestCase(unittest.TestCase):

    def test_add(self):
        addition = unit_test_examples.add(10, 30)
        self.assertEqual(addition, 40)

    def test_sub(self):
        substraction = unit_test_examples.sub(30, 20)
        self.assertEqual(substraction, 10)

# if __name__ == '__main__':
#     unittest.main()
