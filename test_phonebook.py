"""Contains crud tests for phonebook"""

import unittest

from phonebook import Phonebook

class TestPhonebookCase(unittest.TestCase):
    """
    Tests whether user can create, 
    view, update and delete contacts
    """
    def setUp(self):
        """Initialize objects to work with"""
        self.contact_list = []    
        self.cont1 = Phonebook('Peter', '0712705422')
        self.cont2 = Phonebook('Tony', '0719121212')
    def tearDown(self):
        del self.cont1
        del self.cont2
        del self.contact_list



