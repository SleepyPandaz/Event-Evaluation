from django.test import TestCase

# Create your tests here.
from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse
from .models import Student
from . import views


class StudentPageTests(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('Students'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('Students'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Student/index2.html')

    def test_home_page_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, '<h1>Students</h1>')
        
class StudentTests(TestCase):

    def setUp(self):
        Student.objects.create(text='just a test')

    def test_text_content(self):
        student = Student.objects.get(id=1)
        #expected_object_name = f'{student.text}'
        self.assertEquals(expected_object_name, 'just a test')

    def test_student_list_view(self):
        response = self.client.get(reverse('student'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'just a test')
        self.assertTemplateUsed(response, 'Student/index2.html')