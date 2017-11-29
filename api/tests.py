# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.

from .models import risk_type
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

class ModelTestCase(TestCase):
    """This class defines the test suite for the risk_type model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.risk_type_name = "Write world class code"
        self.risk_type = risk_type(name=self.risk_type_name)

    def test_model_can_create_a_risk_type(self):
        """Test the risk_type model can create a risk_type."""
        old_count = risk_type.objects.count()
        self.risk_type.save()
        new_count = risk_type.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.risk_type_data = {'name': 'Sample Risk Type'}
        self.response = self.client.post(
            reverse('create'),
            self.risk_type_data,
            format="json")

    def test_api_can_create_a_risk_type(self):
        """Test the api has risk_type creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_risk_type(self):
        """Test the api can get a given risk_type."""
        risk_type = risk_type.objects.get()
        response = self.client.get(
            reverse('details',
            kwargs={'pk': risk_type.risk_type_id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, risk_type)

    def test_api_can_update_risk_type(self):
        """Test the api can update a given risk_type."""
        change_risk_type = {'name': 'Something new'}
        res = self.client.put(
            reverse('details', kwargs={'pk': risk_type.risk_type_id}),
            change_risk_type, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_risk_type(self):
        """Test the api can delete a risk_type."""
        risk_type = risk_type.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': risk_type.risk_type_id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)