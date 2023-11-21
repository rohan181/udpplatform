from rest_framework import views, response, exceptions, permissions


from . import services, authentication
from . import serializer as user_serializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


from rest_framework.exceptions import AuthenticationFailed
from .models import User

from django.conf import settings
from django.core.mail import send_mail
import random


    



class UserCreateAPIViewemail(APIView):
    def post(self, request, format=None):
        data = request.data
        user_type = data.get('user_type')

        if user_type == 'parent':
            # Validate the required fields for parent
            required_fields = ['firstname', 'lastname', 'user_type', 'street', 'city', 'state', 'zip_code']
            for field in required_fields:
                if field not in data or not data[field]:
                    return Response({f"{field}": ["This field is required."]}, status=status.HTTP_400_BAD_REQUEST)

            # Create the User object for parent
            user = User.objects.create(
                firstname=data['firstname'],
                lastname=data['lastname'],
                user_type=data['user_type'],
                email=data.get('email'),
                street=data['street'],
                city=data['city'],
                state=data['state'],
                zip_code=data['zip_code'],
            )

            return Response({"id": user.id, "message": "User parent created successfully"}, status=status.HTTP_201_CREATED)

        elif user_type == 'child':
            # Validate the required fields for child
            required_fields_child = ['firstname', 'lastname', 'user_type', 'parent_user']
            for field in required_fields_child:
                if field not in data or not data[field]:
                    return Response({f"{field}": ["This field is required."]}, status=status.HTTP_400_BAD_REQUEST)

            # Create the User object for child with reference to the parent_user
            parent_user_id = data.get('parent_user')
            try:
                parent_user = User.objects.get(id=parent_user_id, user_type='parent')
            except User.DoesNotExist:
                return Response({"parent_user": ["Invalid parent user."]}, status=status.HTTP_400_BAD_REQUEST)

            user = User.objects.create(
                firstname=data['firstname'],
                lastname=data['lastname'],
                user_type=data['user_type'],
                parent_user=parent_user,
            )

            return Response({"id": user.id, "message": "User child created successfully"}, status=status.HTTP_201_CREATED)

        else:
            return Response({"user_type": ["Invalid user type."]}, status=status.HTTP_400_BAD_REQUEST)
        




# class UserUpdateAPIView(APIView):
#     def put(self, request, user_id, format=None):
#         data = request.data
#         user_type = data.get('user_type')

#         # Check if the user with the given ID exists
#         try:
#             user = User.objects.get(id=user_id)
#             typeselected=user.user_type
#         except User.DoesNotExist:
#             return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)
        
#         if user_type == 'parent':
#             # Validate the required fields for parent update
            
#             if typeselected == "parent":
#                 required_fields = ['firstname', 'lastname', 'user_type', 'street', 'city', 'state', 'zip_code']
#                 for field in required_fields:
#                     if field not in data or not data[field]:
#                         return Response({f"{field}": ["This field is required."]}, status=status.HTTP_400_BAD_REQUEST)
#             # Update the User object for parent
#                 user.firstname = data['firstname']
#                 user.lastname = data['lastname']
#                 user.user_type = data['user_type']
#                 user.email = data.get('email')
#                 user.street = data['street']
#                 user.city = data['city']
#                 user.state = data['state']
#                 user.zip_code = data['zip_code']
#                 user.save()

#                 return Response({"id": user.id, "message": "User parent updated successfully"}, status=status.HTTP_200_OK)
#             if typeselected == "child":

            
#                     required_fields = ['firstname', 'lastname','user_type']
#                     for field in required_fields:
#                         if field not in data or not data[field]:
#                             return Response({f"{field}": ["This field is required."]}, status=status.HTTP_400_BAD_REQUEST)
#                     user.firstname = data['firstname']
#                     user.lastname = data['lastname']
#                     user.user_type = data['user_type']
#                     user.email = data.get('email')
#                     user.street = None
#                     user.city = None
#                     user.state = None
#                     user.zip_code = None
#                     user.save()
#                     return Response({"id": user.id, "message": "User parent updated successfully to child"}, status=status.HTTP_200_OK)


#         if user_type == 'child':
#             # Validate the required fields for child update
           

#             # Update the User object for child with reference to the parent_user
#             parent_user_id = data.get('parent_user')
#             try:
#                 parent_user = User.objects.get(id=parent_user_id, user_type='parent')
#             except User.DoesNotExist:
#                 return Response({"parent_user": ["Invalid parent user."]}, status=status.HTTP_400_BAD_REQUEST)
#             if typeselected =="child":

#                 required_fields_child = ['firstname', 'lastname', 'user_type', 'parent_user']
#                 for field in required_fields_child:
#                     if field not in data or not data[field]:
#                         return Response({f"{field}": ["This field is required."]}, status=status.HTTP_400_BAD_REQUEST)
#                 user.firstname = data['firstname']
#                 user.lastname = data['lastname']
#                 user.user_type = data['user_type']
#                 user.parent_user = parent_user
#                 user.save()

#                 return Response({"id": user.id, "message": "User child updated successfully"}, status=status.HTTP_200_OK)
#             if typeselected =="parent":
#                 required_fields_child = ['firstname', 'lastname', 'user_type', 'street', 'city', 'state', 'zip_code']
#                 for field in required_fields_child:
#                     if field not in data or not data[field]:
#                         return Response({f"{field}": ["This field is required."]}, status=status.HTTP_400_BAD_REQUEST)
#                 print(data['street'])
#                 user.firstname = data['firstname']
#                 user.lastname = data['lastname']
#                 user.user_type = data['user_type']
#                 user.email = data.get('email')
#                 user.street = data['street']
#                 user.city = data['city']
#                 user.state = data['state']
#                 user.zip_code = data['zip_code']
#                 user.save()

#                 return Response({"id": user.id, "message": "User parent updated successfully child to parent"}, status=status.HTTP_200_OK)


#         else:
#             return Response({"user_type": ["Invalid user type."]}, status=status.HTTP_400_BAD_REQUEST)




# class UserUpdateAPIView(APIView):
#     def put(self, request, user_id, format=None):
#         data = request.data
#         user_type = data.get('user_type')
#         try:
#             user = User.objects.get(id=user_id)
#             typeselected = user.user_type
#         except User.DoesNotExist:
#             return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

#         if user_type == 'parent':
#             if typeselected == "parent":
#                 required_fields = ['firstname', 'lastname', 'user_type', 'street', 'city', 'state', 'zip_code']
#                 for field in required_fields:
#                     if field not in data or not data[field]:
#                         return Response({f"{field}": ["This field is required."]}, status=status.HTTP_400_BAD_REQUEST)

#                 user.firstname = data['firstname']
#                 user.lastname = data['lastname']
#                 user.user_type = data['user_type']
#                 user.email = data.get('email')
#                 user.street = data['street']
#                 user.city = data['city']
#                 user.state = data['state']
#                 user.zip_code = data['zip_code']
#                 user.save()

#                 return Response({"id": user.id, "message": "User parent updated successfully"}, status=status.HTTP_200_OK)

#             elif typeselected == "child":
#                 required_fields = ['firstname', 'lastname', 'user_type']
#                 for field in required_fields:
#                     if field not in data or not data[field]:
#                         return Response({f"{field}": ["This field is required."]}, status=status.HTTP_400_BAD_REQUEST)

#                 user.firstname = data['firstname']
#                 user.lastname = data['lastname']
#                 user.user_type = data['user_type']
#                 user.email = data.get('email')
#                 user.street = ''
#                 user.city = ''
#                 user.state = ''
#                 user.zip_code = ''
#                 user.save()
#                 return Response({"id": user.id, "message": "User parent updated successfully to child"}, status=status.HTTP_200_OK)

#         elif user_type == 'child':
#             required_fields_child = ['firstname', 'lastname', 'user_type', 'parent_user']
#             for field in required_fields_child:
#                 if field not in data or not data[field]:
#                     return Response({f"{field}": ["This field is required."]}, status=status.HTTP_400_BAD_REQUEST)

#             parent_user_id = data.get('parent_user')
#             try:
#                 parent_user = User.objects.get(id=parent_user_id, user_type='parent')
#             except User.DoesNotExist:
#                 return Response({"parent_user": ["Invalid parent user."]}, status=status.HTTP_400_BAD_REQUEST)

#             if typeselected == "child":
#                 user.firstname = data['firstname']
#                 user.lastname = data['lastname']
#                 user.user_type = data['user_type']
#                 user.parent_user = parent_user
#                 user.save()

#                 return Response({"id": user.id, "message": "User child updated successfully"}, status=status.HTTP_200_OK)
            
#             elif typeselected == "parent":
#                 user.firstname = data['firstname']
#                 user.lastname = data['lastname']
#                 user.user_type = data['user_type']
#                 user.email = data.get('email')
#                 user.street = data['street']
#                 user.city = data['city']
#                 user.state = data['state']
#                 user.zip_code = data['zip_code']
#                 user.save()

#                 return Response({"id": user.id, "message": "User parent updated successfully child to parent"}, status=status.HTTP_200_OK)

#         else:
#             return Response({"user_type": ["Invalid user type."]}, status=status.HTTP_400_BAD_REQUEST)





class UserUpdateAPIView(APIView):
    def put(self, request, user_id, format=None):
        data = request.data
       
        try:
            user = User.objects.get(id=user_id)
            typeselected = user.user_type
        except User.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)
        
        
       
        user_type = data['user_type']
       
        

        if typeselected =="child" and user_type =="child":
            parent_user_id = data.get('parent_user')
            try:
                parent_user1 = User.objects.get(id=parent_user_id, user_type='parent')
            except User.DoesNotExist:
                return Response({"parent_user": ["Invalid parent user."]}, status=status.HTTP_400_BAD_REQUEST)


            user.firstname = data['firstname']
            user.lastname = data['lastname']
            user.user_type = data['user_type']
            user.parent_user = parent_user1
            user.save()

            return Response({"id": user.id, "message": "User child to child updated successfully"}, status=status.HTTP_200_OK)
        
        elif typeselected =="child" and user_type =="parent":
            user.firstname = data['firstname']
            user.lastname = data['lastname']
            user.user_type = data['user_type']
            user.email = data.get('email')
            user.street = data['street']
            user.city = data['city']
            user.state = data['state']
            user.zip_code = data['zip_code']
            user.save()

            return Response({"id": user.id, "message": "User parent updated successfully child to parent"}, status=status.HTTP_200_OK)
        
        elif typeselected =="parent" and user_type =="parent":
            user.firstname = data['firstname']
            user.lastname = data['lastname']
            user.user_type = data['user_type']
            user.email = data.get('email')
            user.street = data['street']
            user.city = data['city']
            user.state = data['state']
            user.zip_code = data['zip_code']
            user.save()

            return Response({"id": user.id, "message": "User parent updated successfully parent to parent"}, status=status.HTTP_200_OK)
        
        elif typeselected =="parent" and user_type =="child":
            parent_user_id = data.get('parent_user')
            try:
                parent_user1 = User.objects.get(id=parent_user_id, user_type='parent')
            except User.DoesNotExist:
                return Response({"parent_user": ["Invalid parent user."]}, status=status.HTTP_400_BAD_REQUEST)

            user.firstname = data['firstname']
            user.lastname = data['lastname']
            user.user_type = data['user_type']
            user.email = data.get('email')
            user.parent_user = parent_user1
            user.save()

            return Response({"id": user.id, "message": "User parent updated successfully parent to child"}, status=status.HTTP_200_OK)
        






            




class UserDeleteAPIView(APIView):
    def delete(self, request, user_id, format=None):
        # Check if the user with the given ID exists
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        # Delete the user
        user.delete()

        return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)       
        
    







