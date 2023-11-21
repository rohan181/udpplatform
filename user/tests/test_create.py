# your_app/tests/test_views.py

from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()



class TestUserCreateAPIView(APITestCase):
    def test_create_parent_user(self):
        url = reverse('create-user')
        data = {
            'user_type': 'parent',
            'firstname': 'John',
            'lastname': 'Doe',
            'email': 'john@example.com',
            'street': '123 Main St',
            'city': 'City',
            'state': 'State',
            'zip_code': '12345',
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.first().user_type, 'parent')

    def test_create_child_userwithparent(self):
    # Assuming a parent user already exists
        parent_user = User.objects.create_user(
            user_type='parent',
            firstname='Parent',
            lastname='User',
            email='parent@example.com',  # Add the email field
            street='666',
            city='aaa',
            state='kkk',
            zip_code='hellp')

        url = reverse('create-user')
        data = {
            'user_type': 'child',
            'firstname': 'Child',
            'lastname': 'User',
            'parent_user': parent_user.id,
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(User.objects.last().user_type, 'child')


    def test_create_child_userwithparentwithout(self):
    # Assuming a parent user already exists
        parent_user = User.objects.create_user(
            user_type='child',
            firstname='Parent',
            lastname='User',
            email='parent@example.com',  # Add the email field
            
        
            )

        url = reverse('create-user')
        data = {
            'user_type': 'child',
            'firstname': 'Child',
            'lastname': 'User',
            'parent_user': parent_user.id,
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        

    def test_invalid_user_type(self):
            url = reverse('create-user')
            data = {
                'user_type': 'invalid',
                
            }

            response = self.client.post(url, data, format='json')
            print(response.content)
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertIn('user_type', response.data)
