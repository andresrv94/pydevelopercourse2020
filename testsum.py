import unittest
import sumfortest

class TestMain(unittest.TestCase):

    def setUp(self):
        print("Testing functions...")

    def test1(self):
        test_param1 = 10
        test_param2 = 20
        result = sumfortest.sum1(test_param1,test_param2)
        self.assertEqual(result,32)

    def test2(self):
        test_param1 = 10
        test_param2 = 25
        result = sumfortest.sum2(test_param1,test_param2)
        self.assertEqual(result,35)
        

unittest.main()

