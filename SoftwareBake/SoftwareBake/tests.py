import datetime

from django.utils import timezone
from django.test import TestCase
from django.urls import reverse



class QuestionModelTests(TestCase):

    def test_testMethod(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        self.assertIs(time, time)

