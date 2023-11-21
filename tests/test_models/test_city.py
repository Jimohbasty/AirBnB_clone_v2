#!/usr/bin/python3
"""
This script contains test cases for the City class.
"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class TestCity(test_basemodel):
    """
    TestCity class for testing the City model.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a TestCity object.
        """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """
        Test the state_id attribute of the City class.
        """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """
        Test the name attribute of the City class.
        """
        new = self.value()
        self.assertEqual(type(new.name), str)
