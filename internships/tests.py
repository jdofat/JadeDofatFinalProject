# just in case- tests to make sure pages load
# basic testing

from django.test import TestCase
from django.urls import reverse

class SimplePageTests(TestCase):

    def test_home_page_loads(self):
        # go to home page
        response = self.client.get(reverse('home'))
        # check status
        self.assertEqual(response.status_code, 200)
        # does text appear?
        self.assertContains(response, "Welcome")

    def test_results_page_loads(self):
        # to results page
        response = self.client.get(reverse('results'))
        # status is 200 OK?
        self.assertEqual(response.status_code, 200)
        # page has the title?
        self.assertContains(response, "Internships")
