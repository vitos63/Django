from django.test import TestCase
from django.urls import reverse
class SomeTests(TestCase):
    def setUp(self) -> None:
        return super().setUp()
    
    def tearDown(self) -> None:
        return super().tearDown()
    
    def test_home(self):
        path = reverse('home')
        response = self.client.get(path)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'women_app/index.html')
        
