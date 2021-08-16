"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
"""

import django
from django.test import TestCase
from .password import Password

# TODO: Configure your database in settings.py and sync before running tests.

class ViewTest(TestCase):
    """Tests for the application views."""

    if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS
        @classmethod
        def setUpClass(cls):
            super(ViewTest, cls).setUpClass()
            django.setup()

    def test_home(self):
        """Tests the home page."""
        response = self.client.get('/')
        self.assertContains(response, 'Home Page', 1, 200)

    def test_banned_password(self):
        """Tests the banned password list."""
        word = Password("Password123")
        self.assertLess(word.strengthScore, 20)

    def test_balladhealth_password(self):
        """Tests if password related to Ballad Health is not a Strong password."""
        word = Password("BHealth2022!")
        self.assertLess(word.strengthScore, 60)