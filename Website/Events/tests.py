from django.test import TestCase

# Create your tests here.
from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse

from . import views


class EventPageTests(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('Events'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('Events'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Events.html')

    def test_home_page_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, '<h1>Events</h1>')
