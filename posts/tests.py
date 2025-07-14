from django.test import TestCase

# Create your tests here.
from .models import Post
from django.urls import reverse

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text='sample test case')

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_value = f'{post.text}'
        self.assertEqual(expected_value, 'sample test case')

class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text = '2nd test case')
    
    def test_view_by_loc(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code , 200)
    
    def test_view_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code , 200)
    
    def test_view_uses_valid_template(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code , 200)
        self.assertTemplateUsed(response, 'home.html')