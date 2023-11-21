# your_app/tests/test_views.py

from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class TestUserUpdateAPIView(APITestCase):
    

    def test_update_parent_to_parent(self):

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

        url = reverse('user-update', args=[parent_user.id])
        data = data = {
            'user_type': 'parent',
            'firstname': 'UpdatedFirstName',
            'lastname': 'UpdatedLastName',
            'email': 'updated@example.com',
            'street': '456 Updated St',
            'city': 'UpdatedCity',
            'state': 'UpdatedState',
            'zip_code': '54321',
        }
        response = self.client.put(url, data, format='json')
        print(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()  # Refresh the user instance from the database
        self.assertEqual(self.user.firstname, 'UpdatedFirstName')
        self.assertEqual(self.user.lastname, 'UpdatedLastName')
        self.assertEqual(self.user.email, 'updated@example.com')
        self.assertEqual(self.user.street, '456 Updated St')
        self.assertEqual(self.user.city, 'UpdatedCity')
        self.assertEqual(self.user.state, 'UpdatedState')
        self.assertEqual(self.user.zip_code, '54321')
        self.assertEqual(self.user.user_type, 'parent')



    def test_update_parent_to_child(self):
    # Create a parent user
        parent_user = User.objects.create_user(
            user_type='parent',
            firstname='Parent',
            lastname='User',
            email='parent@example.com',
            street='666',
            city='aaa',
            state='kkk',
            zip_code='hellp'
        )
        self.user = parent_user

        # Create another parent user as the target parent user
        parent_user_target = User.objects.create_user(
            user_type='parent',
            firstname='TargetParent',
            lastname='User',
            email='targetparent@example.com',
            street='888',
            city='bbb',
            state='ccc',
            zip_code='world'
        )

        url = reverse('user-update', args=[self.user.id])
        data = {
            'user_type': 'child',
            'firstname': 'UpdatedFirstName',
            'lastname': 'UpdatedLastName',
            'email': 'updated@example.com',
            'parent_user': parent_user_target.id
        }

        response = self.client.put(url, data, format='json')
        print(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.firstname, 'UpdatedFirstName')
        self.assertEqual(self.user.lastname, 'UpdatedLastName')
        
        self.assertEqual(self.user.user_type, 'child')
        self.assertEqual(self.user.parent_user, parent_user_target)

        


    def test_update_child_to_child(self):
    # Create a parent user
        parent_user1 = User.objects.create_user(
            user_type='parent',
            firstname='Parent',
            lastname='User',
            
        )

        # Create a child user with the parent_user field set to parent_user1
        child_user = User.objects.create_user(
            user_type='child',
            firstname='Child',
            lastname='User',
            parent_user=parent_user1
            
        )

        # Set the user for the test
        self.user = child_user

        # Define the update data
        data = {
            'user_type': 'child',
            'firstname': 'UpdatedFirstName',
            'lastname': 'UpdatedLastName',
            'parent_user': parent_user1.id,
            
        }

        # Get the URL for updating the user
        url = reverse('user-update', args=[child_user.id])

        # Make the update request
        response = self.client.put(url, data, format='json')
        print(response.content)
        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Refresh the user instance from the database
        self.user.refresh_from_db()

        # Check if the user attributes are updated correctly
        self.assertEqual(self.user.firstname, 'UpdatedFirstName')
        self.assertEqual(self.user.lastname, 'UpdatedLastName')
        self.assertEqual(self.user.user_type, 'child')  
        self.assertEqual(self.user.parent_user, parent_user1)   




    def test_update_child_to_parent(self):
    # Create a parent user
        parent_user1 = User.objects.create_user(
            user_type='parent',
            firstname='Parent',
            lastname='User',
        )

        # Create a child user with the parent_user field set to parent_user1
        child_user = User.objects.create_user(
            user_type='child',
            firstname='Child',
            lastname='User',
            parent_user=parent_user1
        )

        # Set the user for the test
        self.user = child_user

        # Define the update data
        data = {
            'user_type': 'parent',
            'firstname': 'UpdatedFirstName',
            'lastname': 'UpdatedLastName',
            'email': 'updated@example.com',
            'street': '456 Updated St',
            'city': 'UpdatedCity',
            'state': 'UpdatedState',
            'zip_code': '54321',
        }

        # Get the URL for updating the user
        url = reverse('user-update', args=[self.user.id])

        # Make the update request
        response = self.client.put(url, data, format='json')
        print(response.content)
        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Refresh the user instance from the database
        self.user.refresh_from_db()

        # Check if the user attributes are updated correctly
        self.assertEqual(self.user.firstname, 'UpdatedFirstName')
        self.assertEqual(self.user.lastname, 'UpdatedLastName')
         
        self.assertEqual(self.user.email, 'updated@example.com')
        self.assertEqual(self.user.street, '456 Updated St')
        self.assertEqual(self.user.city, 'UpdatedCity')
        self.assertEqual(self.user.state, 'UpdatedState')
        self.assertEqual(self.user.zip_code, '54321')
        self.assertEqual(self.user.user_type, 'parent')



    def test_update_parent_to_wrong(self):

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

        url = reverse('user-update', args=[parent_user.id])
        data = data = {
            'user_type': 'wrong',
            'firstname': 'UpdatedFirstName',
            'lastname': 'UpdatedLastName',
            'email': 'updated@example.com',
            'street': '456 Updated St',
            'city': 'UpdatedCity',
            'state': 'UpdatedState',
            'zip_code': '54321',
        }
        response = self.client.put(url, data, format='json')
        print(response.content)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)   


    def test_update_child_to_wrong(self):

       parent_user1 = User.objects.create_user(
            user_type='parent',
            firstname='Parent',
            lastname='User',
            
        )

        # Create a child user with the parent_user field set to parent_user1
       child_user = User.objects.create_user(
            user_type='child',
            firstname='Child',
            lastname='User',
            parent_user=parent_user1
            
        )

        # Set the user for the test
       self.user = child_user

        # Define the update data
       data = {
            'user_type': 'wrong',
            'firstname': 'UpdatedFirstName',
            'lastname': 'UpdatedLastName',
            'parent_user': parent_user1.id,
            
        }

        # Get the URL for updating the user
       url = reverse('user-update', args=[child_user.id])

        # Make the update request
       response = self.client.put(url, data, format='json')
       response = self.client.put(url, data, format='json')
       print(response.content)
       self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)      




            
        
    
