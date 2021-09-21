import unittest
import my_fib_module


class TestFib(unittest.TestCase):
    def test_fib_1(self):
        self.assertEqual(my_fib_module.fib(1), 1)

    def test_fib_2(self):
        self.assertEqual(my_fib_module.fib(2), 1)

    def test_fib3(self):
        self.assertEqual(my_fib_module.fib(3), 2)

    def test_fib_4(self):
        self.assertEqual(my_fib_module.fib(4), 3)

    def test_fib_5(self):
        self.assertEqual(my_fib_module.fib(5), 5)

    def test_fib_6(self):
        self.assertEqual(my_fib_module.fib(6), 8)

    def test_fib_7(self):
        self.assertEqual(my_fib_module.fib(7), 13)

    def test_fib_8(self):
        self.assertEqual(my_fib_module.fib(8), 21)

    def test_fib_9(self):
        self.assertEqual(my_fib_module.fib(9), 34)

    def test_fib_10(self):
        self.assertEqual(my_fib_module.fib(10), 55)

    def test_fib_11(self):
        self.assertEqual(my_fib_module.fib(11), 89)

    def test_fib_12(self):
        self.assertEqual(my_fib_module.fib(12), 144)

    def test_fib_13(self):
        self.assertEqual(my_fib_module.fib(13), 233)

    def test_fib_14(self):
        self.assertEqual(my_fib_module.fib(14), 377)

    def test_fib_15(self):
        self.assertEqual(my_fib_module.fib(15), 610)

    def test_fib_16(self):
        self.assertEqual(my_fib_module.fib(16), 987)

    def test_fib_17(self):
        self.assertEqual(my_fib_module.fib(17), 1597)

    def test_fib_18(self):
        self.assertEqual(my_fib_module.fib(18), 2584)

    def test_fib_19(self):
        self.assertEqual(my_fib_module.fib(19), 4181)

    def test_fib_20(self):
        self.assertEqual(my_fib_module.fib(20), 6765)


if __name__ == "__main__":
    unittest.main()
