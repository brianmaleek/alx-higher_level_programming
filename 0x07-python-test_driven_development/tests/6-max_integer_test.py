#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class to test max_integer"""
    def test_module_docstring(self):
        """Test for the existence of module docstring"""
        module_doc = __import__('6-max_integer').__doc__
        self.assertTrue(len(module_doc) > 1)

    def test_function_docstring(self):
        """Test for the existence of function docstring"""
        function_doc = __import__('6-max_integer').max_integer.__doc__
        self.assertTrue(len(function_doc) > 1)

    def test_signed_ints_and_floats(self):
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 3, -4]), 3)
        self.assertEqual(max_integer([-1.5, -2.5]), -1.5)
        self.assertEqual(max_integer([10, -10, 10]), 10)
        self.assertEqual(max_integer([{1, 9}, {2}, {3}]), {1, 9})

    def test_lists(self):
        self.assertEqual(max_integer([[1, 2], [1, 3]]), [1, 3])
        self.assertEqual(max_integer([[1, 2], [1, 4]]), [1, 4])

    def test_list_of_strings(self):
        self.assertEqual(max_integer("1234"), '4')
        self.assertEqual(max_integer("abcdef"), 'f')
        self.assertEqual(max_integer(['a', 'b', 'c', 'x', 'y', 'z']), 'z')
        self.assertEqual(max_integer(["abc", 'x']), 'x')

    def test_empty_strings(self):
        self.assertIsNone(max_integer(""), None)
        self.assertIsNone(max_integer([]), None)

    def test_other_sequences(self):
        with self.assertRaises(TypeError):
            max_integer({1, 2}, {3, 4, 5})
        with self.assertRaises(TypeError):
            max_integer({1, 2, 3, 4, 5})
        with self.assertRaises(TypeError):
            max_integer([-10, 0.5, "str", {1, 2}])
        with self.assertRaises(TypeError):
            max_integer([None, True])

    def test_None(self):
        self.assertIsNone(max_integer([]), None)
        self.assertIsNone(max_integer(), None)
        self.assertIsNone(max_integer([None]), None)

if __name__ == "__main__":
    unittest.main()
