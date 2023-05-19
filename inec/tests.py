from django.test import TestCase
from django.urls import reverse
from .models import PollingUnit

class HomeListViewTest(TestCase):
    def setUp(self):
        self.url = reverse('home')

    def test_home_list_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

class PollDetailViewTest(TestCase):
    def setUp(self):
        self.polling_unit = PollingUnit.objects.create(polling_unit_name='Polling Unit 1')
        self.url = reverse('poll_detail', args=[self.polling_unit.pk])

    def test_poll_detail_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'detail.html')
        self.assertContains(response, self.polling_unit.polling_unit_name)

class LocalGovResultsViewTest(TestCase):
    def setUp(self):
        self.url = reverse('local_gov_results')

    def test_local_gov_results_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'results.html')

    def test_local_gov_results_view_post(self):
        # Assuming a valid LGA ID
        data = {'lga': '1'}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)  # Assuming it redirects to 'results'
        self.assertRedirects(response, reverse('results'))

class SearchViewTest(TestCase):
    def setUp(self):
        self.url = reverse('search')

    def test_search_view(self):
        data = {'item': 'Polling Unit'}
        response = self.client.get(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search.html')

class CreateUnitViewTest(TestCase):
    def setUp(self):
        self.url = reverse('new_polling_unit')
        self.form_data = {
            'polling_unit_name': 'New Polling Unit',
            # Provide other required form fields' data
        }

    def test_create_unit_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_post.html')

    def test_create_unit_view_post(self):
        response = self.client.post(self.url, data=self.form_data)
        self.assertEqual(response.status_code, 200)  # Assuming successful form submission
        # Additional assertions for successful form submission
