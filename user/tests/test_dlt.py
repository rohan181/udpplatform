
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


User = get_user_model()

class UserDeleteAPIViewTest(APITestCase):
   

    def test_delete_user_success(self):
        # Get the URL for deleting the user


        parent_user = User.objects.create_user(
            user_type='parent',
            firstname='Parent',
            lastname='User',
            email='parent@example.com',  # Add the email field
            street='666',
            city='aaa',
            state='kkk',
            zip_code='hellp'
        
            )
        self.user = parent_user
        url = reverse('user-delete', args=[self.user.id])

        # Make the delete request
        response = self.client.delete(url)

        # Check if the response status code is 204 NO CONTENT
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Check if the user has been deleted from the database
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(id=self.user.id)

    def test_delete_nonexistent_user(self):


        parent_user = User.objects.create_user(
            user_type='parent',
            firstname='Parent',
            lastname='User',
            email='parent@example.com',  # Add the email field
            street='666',
            city='aaa',
            state='kkk',
            zip_code='hellp'
        
            )
        self.user = parent_user
        # Get an ID that doesn't exist in the database
        nonexistent_user_id = self.user.id + 1

        # Get the URL for deleting the nonexistent user
        url = reverse('user-delete', args=[nonexistent_user_id])

        # Make the delete request
        response = self.client.delete(url)

        # Check if the response status code is 404 NOT FOUND
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        # Check if the response contains the expected detail message
        self.assertEqual(response.data, {"detail": "User not found."})
