#!/usr/bin/python3

"""Unittests for rectangle.py"""

from unittest.mock import patch
import unittest
import json
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Rectangle class tests"""

    def setUp(self):
        """Resets nb_objects to 0"""
        Base._Base__nb_objects = 0

    def test_is_subclass(self):
        """Test if Rectangle is subclass of Base"""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_new_rectangle(self):
        """Test creating a new rectangle"""
        new = Rectangle(1, 2)
        self.assertEqual(new.id, 1)
        self.assertEqual(new.width, 1)
        self.assertEqual(new.height, 2)
        self.assertEqual(new.x, 0)
        self.assertEqual(new.y, 0)

    def test_custom_values(self):
        """Test creating a rectangle with custom values"""
        new2 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(new2.id, 5)
        self.assertEqual(new2.width, 1)
        self.assertEqual(new2.height, 2)
        self.assertEqual(new2.x, 3)
        self.assertEqual(new2.y, 4)

    def test_equality(self):
        """Test that two rectangles with the same values are not the same object"""
        new3 = Rectangle(1, 1, 1, 1)
        new4 = Rectangle(1, 1, 1, 1)
        self.assertFalse(new3 is new4)
        self.assertFalse(new3 == new4)

    def test_incorrect_attributes(self):
        """Test for attributes as strings and negative values"""
        with self.assertRaises(TypeError):
            Rectangle("string", 1)
        with self.assertRaises(TypeError):
            Rectangle(1, "string")

    def test_zero_attributes(self):
        """Test attributes as negative and zero"""
        with self.assertRaises(ValueError):
            Rectangle(-1, 1)
        with self.assertRaises(ValueError):
            Rectangle(1, -1)
        with self.assertRaises(ValueError):
            Rectangle(1, 1, -1)
        with self.assertRaises(ValueError):
            Rectangle(1, 1, 1, -1)
        with self.assertRaises(ValueError):
            Rectangle(0, 1)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_wrong_amount_of_attributes(self):
        """Test for wrong amount of attributes"""
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 1, 1, 1, 1)
        with self.assertRaises(TypeError):
            Rectangle(1)
        with self.assertRaises(TypeError):
            Rectangle()

    def test_area(self):
        """Test for area"""
        new19 = Rectangle(2, 3)
        self.assertEqual(new19.area(), 6)
        new20 = Rectangle(2, 3, 4, 5, 6)
        self.assertEqual(new20.area(), 6)
        new20.width = 10
        self.assertEqual(new20.area(), 30)
        new20.height = 10
        self.assertEqual(new20.area(), 100)
        new20.x = 10
        self.assertEqual(new20.area(), 100)
        new20.y = 10
        self.assertEqual(new20.area(), 100)

    def test_display(self):
        """Test for display"""
        new21 = Rectangle(2, 3)
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            new21.display()
            self.assertEqual(fakeOutput.getvalue(), "##\n##\n##\n")

    def test_str(self):
        """Test for __str__ method"""
        new23 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(new23.__str__(), "[Rectangle] (12) 2/1 - 4/6")
        new24 = Rectangle(4, 6, 2, 1)
        self.assertEqual(new24.__str__(), "[Rectangle] (1) 2/1 - 4/6")

    def test_update(self):
        """Test for update"""
        new25 = Rectangle(10, 10, 10, 10)
        new25.update(89)
        self.assertEqual(new25.__str__(), "[Rectangle] (89) 10/10 - 10/10")
        new25.update(89, 2)
        self.assertEqual(new25.__str__(), "[Rectangle] (89) 10/10 - 2/10")
        new25.update(89, 2, 3)
        self.assertEqual(new25.__str__(), "[Rectangle] (89) 10/10 - 2/3")
        new25.update(89, 2, 3, 4)
        self.assertEqual(new25.__str__(), "[Rectangle] (89) 4/10 - 2/3")
        new25.update(89, 2, 3, 4, 5)
        self.assertEqual(new25.__str__(), "[Rectangle] (89) 4/5 - 2/3")

    def test_dictionary(self):
        """Test for to_dictionary method"""
        new27 = Rectangle(3, 5, 1, 2, 3)
        res = {'x': 1, 'y': 2, 'id': 3, 'height': 5, 'width': 3}
        self.assertEqual(new27.to_dictionary(), res)
        new28 = Rectangle(3, 5, 1, 2, 3)
        new28.update(89, 2, 3, 4, 5)
        res = {'x': 4, 'y': 5, 'id': 89, 'height': 3, 'width': 2}
        self.assertEqual(new28.to_dictionary(), res)

    def test_dict_to_json(self):
        """Test for dictionary to json method"""
        new27 = Rectangle(3, 5, 1, 2, 3)
        res = new27.to_dictionary()
        self.assertEqual(type(Base.to_json_string([res])), str)

    def test_create(self):
        """Test for create method"""
        new27 = Rectangle(3, 5, 1, 2, 3)
        new28 = Rectangle.create(**new27.to_dictionary())
        self.assertEqual(new27.__str__(), new28.__str__())
        self.assertFalse(new27 is new28)
        self.assertFalse(new27 == new28)

    def test_load_from_file(self):
        """Test for load_from_file method"""
        new29 = Rectangle(3, 5, 1, 2, 3)
        new30 = Rectangle(4, 6, 2, 3, 4)
        list1 = [new29, new30]
        Rectangle.save_to_file(list1)
        list2 = Rectangle.load_from_file()
        self.assertEqual(list2[0].__str__(), "[Rectangle] (3) 1/2 - 3/5")
        self.assertEqual(list2[1].__str__(), "[Rectangle] (4) 2/3 - 4/6")
        self.assertFalse(list1 is list2)
        self.assertFalse(list1 == list2)

    def test_save_to_file(self):
        """Test for save_to_file method"""
        new33 = Rectangle(3, 5, 1, 2, 3)
        new34 = Rectangle(4, 6, 2, 3, 4)
        list1 = [new33, new34]
        Rectangle.save_to_file(list1)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(type(file.read()), str)

    def test_save_to_file2(self):
        """Test for save_to_file method with None"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file3(self):
        """Test for save_to_file method with an empty list"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")


if __name__ == '__main__':
    unittest.main()
