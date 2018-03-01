"""Contains crud tests for phonebook"""

import unittest

from app.models import Phonebook

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

    def test_create_contact(self):
        """Test app can create a contact"""
        response = self.cont1.create_contact(self.contact_list)
        self.assertTrue(response['message'], "Contact successfuly created")
    
    def test_view_contacts(self):
        """Test app can return all contacts created"""
        self.cont1.create_contact(self.contact_list)
        self.cont2.create_contact(self.contact_list)
        self.assertTrue(len(self.contact_list), 2)
        response = Phonebook.view_contacts(self.contact_list)
        self.assertTrue({'name':'peter','name':'Tony'}, response)

    def test_update_contact(self):
        """Test app can update contact"""
        self.cont1.create_contact(self.contact_list)
        response = self.cont1.update_contact(self.contact_list, contact='0733333333')
        self.assertTrue(response, {'name':'Peter', 'contact':'0733333333'})

    def test_delete_contact(self):
        """Test app can delete contact effectively"""
        self.cont1.create_contact(self.contact_list)
        self.cont2.create_contact(self.contact_list)
        response = self.cont1.delete_contact(self.contact_list)
        self.assertTrue(response)
        self.assertTrue(self.contact_list, [{'name':'Tony', 'contact':'0719121212'}])
        
    
        
