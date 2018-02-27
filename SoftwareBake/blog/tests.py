import datetime

from django.utils import timezone
from django.test import TestCase
from django.urls import reverse

class SimpleTest(TestCase):
    """Tests for the application views."""

    ## Django requires an explicit setup() when running tests in PTVS
    #@classmethod
    #def setUpClass(cls):
    #    django.setup()

    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
