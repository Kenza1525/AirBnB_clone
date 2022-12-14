#!/usr/bin/python3
"""Test of Review Class """

from models.review import Review
import unittest


class TestReview(unittest.TestCase):
    """ Test User Class """
    model = Review()

    def test_attribute_place_id(self):
        """ Tests attr """
        self.assertEqual(hasattr(self.model, "place_id"), True)
        self.assertEqual(hasattr(self.model, "user_id"), True)
        self.assertEqual(hasattr(self.model, "text"), True)

    def test_types(self):
        """ test types """
        self.assertEqual(type(self.model.place_id), str)
        self.assertEqual(type(self.model.user_id), str)
        self.assertEqual(type(self.model.text), str)

if __name__ == '__main__':
    unittest.main()
