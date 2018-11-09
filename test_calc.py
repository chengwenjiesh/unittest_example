import unittest
import calc

class TestCalc(unittest.TestCase):
    def setUp(self):
        print 'Now setUp'
        self.num1 = 10
        self.num2 = 5
        self.num3 = 0


    def tearDown(self):
        print 'Now tearDown'


    def test_add(self):
        print 'Now test add'
        self.assertEqual(calc.add(self.num1, self.num2), 15)


    def test_div(self):
        print 'Now test div'
        self.assertEqual(calc.div(self.num1, self.num2), 2)
        with self.assertRaises(ValueError):
            calc.div(self.num1, self.num3)


if __name__ == '__main__':
    unittest.main()
