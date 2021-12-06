import unittest

class TestSomething(unittest.TestCase):
    def test_something(self):
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

class TestSomething2(unittest.TestCase):
    def test_something(self):
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)


class TestSomething3(unittest.TestCase):
    def test_something(self):
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)



if __name__ == '__main__':
    unittest.main()