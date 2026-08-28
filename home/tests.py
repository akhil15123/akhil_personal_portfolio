from django.test import TestCase
from django.urls import reverse

from .models import Contact


class PortfolioViewTests(TestCase):
    def test_home_page_renders(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_projects_page_renders(self):
        response = self.client.get(reverse('projects'))
        self.assertEqual(response.status_code, 200)

    def test_contact_submission_is_saved(self):
        response = self.client.post(
            reverse('contact'),
            {
                'name': 'Ada Rivera',
                'email': 'ada@example.com',
                'subject': 'AI collaboration',
                'message': 'I would like to discuss a Python project.',
            },
        )
        self.assertRedirects(response, '/#contact', fetch_redirect_response=False)
        self.assertEqual(Contact.objects.count(), 1)

    def test_incomplete_contact_submission_is_rejected(self):
        response = self.client.post(reverse('contact'), {'name': 'Ada'})
        self.assertRedirects(response, '/#contact', fetch_redirect_response=False)
        self.assertEqual(Contact.objects.count(), 0)
