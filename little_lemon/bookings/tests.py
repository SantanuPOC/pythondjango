from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Menu, TableBooking

class MenuAPITest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu_url = reverse('menu-list')
        self.menu_data = {'name': 'Pizza', 'description': 'Delicious cheese pizza', 'price': 9.99}

    def test_create_menu(self):
        response = self.client.post(self.menu_url, self.menu_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_menu(self):
        self.client.post(self.menu_url, self.menu_data, format='json')
        response = self.client.get(self.menu_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

class TableBookingAPITest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.force_authenticate(user=self.user)
        self.booking_url = reverse('tablebooking-list')
        self.booking_data = {'user': self.user.id, 'date': '2023-10-10', 'time': '18:00:00', 'number_of_people': 4}

    def test_create_booking(self):
        response = self.client.post(self.booking_url, self.booking_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_booking(self):
        self.client.post(self.booking_url, self.booking_data, format='json')
        response = self.client.get(self.booking_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)