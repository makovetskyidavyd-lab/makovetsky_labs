from django.test import TestCase
from django.urls import reverse, resolve
from .views import HomePageView, ArticleList

class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  # Було assertEquals

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEqual(view.func.view_class, HomePageView) # Було assertEquals

class CategoryTest(TestCase):
    def test_category_view_status_code(self):
        url = reverse('articles-category-list', args=('name',))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200) # Було assertEquals

class ArticlesListTest(TestCase):
    def test_articles_list_view_status_code(self):
        url = reverse('articles-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200) # Було assertEquals
    
    def test_articles_list_url_resolves_view(self):
        view = resolve('/articles')
        self.assertEqual(view.func.view_class, ArticleList) # Було assertEquals