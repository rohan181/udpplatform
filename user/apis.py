from rest_framework import views, response, exceptions, permissions


from . import services, authentication
from . import serializer as user_serializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializer import UserCreateSerializerphone,UserCreateSerializeremail,ProfileCreateSerializer,Profileloactionbd,Profileloactionabroad,Profileinfoexperienceserializer,Profilecomplete1Serializer, Profilecomplete2Serializer, Profilecomplete3Serializer, Profilecomplete4Serializer, Profilecomplete5Serializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Profileinfo1,Profileinfolocationbd,Profileinfolocationabroad,Profileinfoexperience
import jwt, datetime
from rest_framework.exceptions import AuthenticationFailed
from .models import User,Profileinfo1, Profilecomplete1, Profilecomplete2, Profilecomplete3, Profilecomplete4, Profilecomplete5

from django.conf import settings
from django.core.mail import send_mail
import random

# class RegisterApi(views.APIView):
#     def post(self, request):
#         serializer = user_serializer.UserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         data = serializer.validated_data
#         serializer.instance = services.create_user(user_dc=data)

#         return response.Response(data=serializer.data)


# class LoginApi(views.APIView):
#     def get(self, request):
#         # email = request.data["email"]
#         # password = request.data["password"]

#         # user = services.user_email_selector(email=email)

#         # if user is None:
#         #     raise exceptions.AuthenticationFailed("Invalid Credentials")

#         # if not user.check_password(raw_password=password):
#         #     raise exceptions.AuthenticationFailed("Invalid pasword Credentials")

#         # payload = {
#         #     'id': user.id,
#         #     'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
#         #     'iat': datetime.datetime.utcnow()
#         # }

#         # token = jwt.encode(payload, 'secret', algorithm='HS256')

#         # response = Response()



#         subject = 'welcome to GFG world'
#         message = f'Hi , thank you for registering in geeksforgeeks.'
#         email_from = settings.EMAIL_HOST_USER

#         email_address = "ab.rohan462@gmail.com"
#         email_tuple = (email_address,) 

#         recipient_list =   email_tuple 
#         send_mail( subject, message, email_from, recipient_list )

#         #response.set_cookie(key='jwt', value=token, httponly=True)
#         response.data = {
#             'jwt': 1
#         }
#         return response
    


class LoginApi(views.APIView):
    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]

        user = services.user_email_selector(email=email)

        if user is None:
            raise exceptions.AuthenticationFailed("not found email")

        if not user.check_password(raw_password=password):
            raise exceptions.AuthenticationFailed("Invalid password")

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=100000),
            'iat': datetime.datetime.utcnow()
        }



        

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response     
    

class LoginApi1(views.APIView):
    def post(self, request):
        phone_number = request.data["phone_number"]
        password = request.data["password"]

        user = services.user_phone_selector(phone_number=phone_number)

        if user is None:
            raise exceptions.AuthenticationFailed("Invalid phone")

        if not user.check_password(raw_password=password):
            raise exceptions.AuthenticationFailed("Invalid Credentials")

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=100000),
            'iat': datetime.datetime.utcnow()
        }



        

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response  


# class UserApi(views.APIView):
#     """
#     This endpoint can only be used
#     if the user is authenticated
#     """

    
#     def get(self, request):
#         token = request.COOKIES.get('jwt')

#         if not token:
#             raise AuthenticationFailed('Unauthenticated!')

#         try:
#             payload = jwt.decode(token, 'secret', algorithm=['HS256'])
#         except jwt.ExpiredSignatureError:
#             raise AuthenticationFailed('Unauthenticated!')

#         user = User.objects.filter(id=payload['id']).first()
#         serializer = user_serializer.UserSerializer(user)
#         return Response(serializer.data)
    



class UserApi(views.APIView):
    """
    This endpoint can only be used if the user is authenticated with a Bearer token
    """

    def get(self, request):
        # Retrieve the JWT token from the Authorization header
        authorization_header = request.headers.get('Authorization')

        if not authorization_header or not authorization_header.startswith('Bearer '):
            raise AuthenticationFailed('Invalid or missing Bearer token!')

        token = authorization_header.split('Bearer ')[1]

        if not token:
            raise AuthenticationFailed('Invalid or missing token!')

        try:
            # Make sure to use the same secret key that was used to encode the JWT
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('JWT has expired!')
        except jwt.DecodeError:
            raise AuthenticationFailed('JWT is invalid!')

        user = User.objects.filter(id=payload['id']).first()

        if not user:
            raise AuthenticationFailed('User not found!')

        # You should import and use your user serializer here
        # serializer = user_serializer.UserSerializer(user)
        # Replace the following line with the one above.
        serializer = user_serializer.UserSerializer(user)

        return Response(serializer.data)    
    


class ViewCreateProfileAPIView(views.APIView):

    def get(self, request):
        # Retrieve the JWT token from the Authorization header
        authorization_header = request.headers.get('Authorization')

        if not authorization_header or not authorization_header.startswith('Bearer '):
            raise AuthenticationFailed('Invalid or missing Bearer token!')

        token = authorization_header.split('Bearer ')[1].strip()  # Strip whitespaces

        try:
            # Make sure to use the same secret key that was used to encode the JWT
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('JWT has expired!')
        except jwt.DecodeError:
            raise AuthenticationFailed('JWT is invalid!')

        user = User.objects.filter(id=payload['id']).first()

        if not user:
            raise AuthenticationFailed('User not found!')

        profile = Profileinfo1.objects.filter(user=user).first()

        if not profile:
            raise AuthenticationFailed('Profile not found!')

        # You should import and use your profile serializer here
        serializer = ProfileCreateSerializer(profile)

        return Response(serializer.data)   
    



class viewProfilelocationbdCreateAPIView(views.APIView):

    def get(self, request):
        # Retrieve the JWT token from the Authorization header
        authorization_header = request.headers.get('Authorization')

        if not authorization_header or not authorization_header.startswith('Bearer '):
            raise AuthenticationFailed('Invalid or missing Bearer token!')

        token = authorization_header.split('Bearer ')[1].strip()  # Strip whitespaces

        try:
            # Make sure to use the same secret key that was used to encode the JWT
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('JWT has expired!')
        except jwt.DecodeError:
            raise AuthenticationFailed('JWT is invalid!')

        user = User.objects.filter(id=payload['id']).first()

        if not user:
            raise AuthenticationFailed('User not found!')

        profile = Profileinfolocationbd.objects.filter(user=user).first()

        if not profile:
            raise AuthenticationFailed('Profile not found!')

        # You should import and use your profile serializer here
        serializer = Profileloactionbd(profile)

        return Response(serializer.data)     


class viewProfilelocationabroadCreateAPIView(views.APIView):

    def get(self, request):
        # Retrieve the JWT token from the Authorization header
        authorization_header = request.headers.get('Authorization')

        if not authorization_header or not authorization_header.startswith('Bearer '):
            raise AuthenticationFailed('Invalid or missing Bearer token!')

        token = authorization_header.split('Bearer ')[1].strip()  # Strip whitespaces

        try:
            # Make sure to use the same secret key that was used to encode the JWT
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('JWT has expired!')
        except jwt.DecodeError:
            raise AuthenticationFailed('JWT is invalid!')

        user = User.objects.filter(id=payload['id']).first()

        if not user:
            raise AuthenticationFailed('User not found!')

        profile = Profileinfolocationabroad.objects.filter(user=user).first()

        if not profile:
            raise AuthenticationFailed('Profile not found!')

        # You should import and use your profile serializer here
        serializer =  Profileloactionabroad(profile)

        return Response(serializer.data)       
    

class viewProfileinfoexperienceCreateAPIView(views.APIView):

    def get(self, request):
        # Retrieve the JWT token from the Authorization header
        authorization_header = request.headers.get('Authorization')

        if not authorization_header or not authorization_header.startswith('Bearer '):
            raise AuthenticationFailed('Invalid or missing Bearer token!')

        token = authorization_header.split('Bearer ')[1].strip()  # Strip whitespaces

        try:
            # Make sure to use the same secret key that was used to encode the JWT
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('JWT has expired!')
        except jwt.DecodeError:
            raise AuthenticationFailed('JWT is invalid!')

        user = User.objects.filter(id=payload['id']).first()

        if not user:
            raise AuthenticationFailed('User not found!')

        profile = Profileinfoexperience.objects.filter(user=user).first()

        if not profile:
            raise AuthenticationFailed('Profile not found!')

        # You should import and use your profile serializer here
        serializer =  Profileinfoexperienceserializer(profile)

        return Response(serializer.data)      




class LogoutApi(views.APIView):
    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        resp = response.Response()
        resp.delete_cookie("jwt")
        resp.data = {"message": "so long farewell"}

        return resp
    



class emailotp(views.APIView):
    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]
        fullname= request.data["fullname"]

        otp = str(random.randint(10000 , 99999))

        payload = {
            'fullname' :fullname,
            'email' :email,
            'password': password,
             'otp' :otp ,
             'email' :email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=4),
            'iat': datetime.datetime.utcnow()
        }
        #otp = str(random.randint(10000 , 99999))
        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()



        subject = 'welcome to GFG world'
        message = f'Hi   otp is,{otp} thank you for registering in probashi'
        email_from = settings.EMAIL_HOST_USER

        email_address = email
        email_tuple = (email_address,) 

        recipient_list =   email_tuple 
        send_mail( subject, message, email_from, recipient_list )

        #response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response



class UserCreateAPIViewphone(APIView):
    def post(self, request, format=None):
        serializer = UserCreateSerializerphone(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



class UserCreateAPIViewemail(APIView):
    def post(self, request, format=None):
        otp_phone = request.data["otp"]
        authorization_header = request.headers.get('Authorization')

        if not authorization_header or not authorization_header.startswith('Bearer '):
            raise AuthenticationFailed('Invalid or missing Bearer token!')

        token = authorization_header.split('Bearer ')[1].strip()  # Strip whitespaces

        try:
            # Make sure to use the same secret key that was used to encode the JWT
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('JWT has expired!')
        except jwt.DecodeError:
            raise AuthenticationFailed('JWT is invalid!')

        email = payload.get('email')
        password = payload.get('password')
        fullname = payload.get('fullname')
        saved_otp = payload.get('otp')  # Get the OTP from the payload

        # Check if the provided OTP matches the saved OTP
        if otp_phone != saved_otp:
            raise AuthenticationFailed('OTP does not match!')

        # Hash the password before saving it
        serializer = UserCreateSerializeremail(data={'email': email, 'password': password, 'fullname': fullname})

        if serializer.is_valid():
            # Save the user object after validation
            user = serializer.save()
            return Response({'message': 'User created successfully.'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)








class CreateProfileAPIView(views.APIView):
    

    def post(self, request):
        # Ensure that the user does not already have a profile

        authorization_header = request.headers.get('Authorization')

        if not authorization_header or not authorization_header.startswith('Bearer '):
            raise AuthenticationFailed('Invalid or missing Bearer token!')

        token = authorization_header.split('Bearer ')[1]

        if not token:
            raise AuthenticationFailed('Invalid or missing token!')

        try:
            # Make sure to use the same secret key that was used to encode the JWT
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('JWT has expired!')
        except jwt.DecodeError:
            raise AuthenticationFailed('JWT is invalid!')

        user1 = User.objects.filter(id=payload['id']).first()

        if not user1:
            raise AuthenticationFailed('User not found!')





        if Profileinfo1.objects.filter(user=user1).exists():
            return Response({'detail': 'Profile already exists for this user.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ProfileCreateSerializer(data=request.data)
        if serializer.is_valid():
            # Create a new profile for the authenticated user
            serializer.save(user=user1)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    





# Subclass the base class for each specific profile creation view


# class CreateProfileAPIView(views.APIView):
#     """
#     This endpoint can only be used if the user is authenticated with a Bearer token
#     """

#     def get(self, request):
#         # Retrieve the JWT token from the Authorization header
#         authorization_header = request.headers.get('Authorization')

#         if not authorization_header or not authorization_header.startswith('Bearer '):
#             raise AuthenticationFailed('Invalid or missing Bearer token!')

#         token = authorization_header.split('Bearer ')[1]

#         if not token:
#             raise AuthenticationFailed('Invalid or missing token!')

#         try:
#             # Make sure to use the same secret key that was used to encode the JWT
#             payload = jwt.decode(token, 'secret', algorithms=['HS256'])
#         except jwt.ExpiredSignatureError:
#             raise AuthenticationFailed('JWT has expired!')
#         except jwt.DecodeError:
#             raise AuthenticationFailed('JWT is invalid!')

#         user = User.objects.filter(id=payload['id']).first()

#         if not user:
#             raise AuthenticationFailed('User not found!')

#         # You should import and use your user serializer here
#         # serializer = user_serializer.UserSerializer(user)
#         # Replace the following line with the one above.
#         serializer = user_serializer.UserSerializer(user)

#         return Response(serializer.data)    




class ProfilelocationbdCreateAPIView(APIView):
    

     def post(self, request):
        # Ensure that the user does not already have a profile

        authorization_header = request.headers.get('Authorization')

        if not authorization_header or not authorization_header.startswith('Bearer '):
            raise AuthenticationFailed('Invalid or missing Bearer token!')

        token = authorization_header.split('Bearer ')[1]

        if not token:
            raise AuthenticationFailed('Invalid or missing token!')

        try:
            # Make sure to use the same secret key that was used to encode the JWT
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('JWT has expired!')
        except jwt.DecodeError:
            raise AuthenticationFailed('JWT is invalid!')

        user1 = User.objects.filter(id=payload['id']).first()

        if not user1:
            raise AuthenticationFailed('User not found!')

        # Ensure that the user does not already have a profile
        if Profileinfolocationbd.objects.filter(user=user1).exists():
            return Response({'detail': 'Profile already exists for this user.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = Profileloactionbd(data=request.data)
        if serializer.is_valid():
            # Create a new profile for the authenticated user
            serializer.save(user=user1)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     
    

class ProfilelocationabroadCreateAPIView(APIView):
    
  def post(self, request):
        # Ensure that the user does not already have a profile

        authorization_header = request.headers.get('Authorization')

        if not authorization_header or not authorization_header.startswith('Bearer '):
            raise AuthenticationFailed('Invalid or missing Bearer token!')

        token = authorization_header.split('Bearer ')[1]

        if not token:
            raise AuthenticationFailed('Invalid or missing token!')

        try:
            # Make sure to use the same secret key that was used to encode the JWT
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('JWT has expired!')
        except jwt.DecodeError:
            raise AuthenticationFailed('JWT is invalid!')

        user1 = User.objects.filter(id=payload['id']).first()

        if not user1:
            raise AuthenticationFailed('User not found!')
        if Profileinfolocationabroad.objects.filter(user=user1).exists():
            return Response({'detail': 'Profile already exists for this user.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = Profileloactionabroad(data=request.data)
        if serializer.is_valid():
            # Create a new profile for the authenticated user
            serializer.save(user=user1)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    



class ProfileinfoexperienceCreateAPIView(APIView):
   

    def post(self, request):
        # Ensure that the user does not already have a profile

        authorization_header = request.headers.get('Authorization')

        if not authorization_header or not authorization_header.startswith('Bearer '):
            raise AuthenticationFailed('Invalid or missing Bearer token!')

        token = authorization_header.split('Bearer ')[1]

        if not token:
            raise AuthenticationFailed('Invalid or missing token!')

        try:
            # Make sure to use the same secret key that was used to encode the JWT
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('JWT has expired!')
        except jwt.DecodeError:
            raise AuthenticationFailed('JWT is invalid!')

        user1 = User.objects.filter(id=payload['id']).first()
        if Profileinfoexperience.objects.filter(user=user1).exists():
            return Response({'detail': 'Profile already exists for this user.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = Profileinfoexperienceserializer(data=request.data)
        if serializer.is_valid():
            # Create a new profile for the authenticated user
            serializer.save(user=user1)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)          
    






class Profilecomplete1ListCreateView(views.APIView):

    def post(self, request):
        # Ensure that the user does not already have a profile

        authorization_header = request.headers.get('Authorization')

        if not authorization_header or not authorization_header.startswith('Bearer '):
            raise AuthenticationFailed('Invalid or missing Bearer token!')

        token = authorization_header.split('Bearer ')[1]

        if not token:
            raise AuthenticationFailed('Invalid or missing token!')

        try:
            # Make sure to use the same secret key that was used to encode the JWT
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('JWT has expired!')
        except jwt.DecodeError:
            raise AuthenticationFailed('JWT is invalid!')

        user1 = User.objects.filter(id=payload['id']).first()

        profile, created = Profilecomplete1.objects.get_or_create(user=user1)

        if not created:
            # If the profile already exists, update the values
            serializer = Profilecomplete1Serializer(profile, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # If the profile was created (not already existing)
        serializer = Profilecomplete1Serializer(data=request.data)
        if serializer.is_valid():
            # Create a new profile for the authenticated user
            serializer.save(user=user1)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    
    





class viewprofilecomplete1(views.APIView):

    def get(self, request):
        # Retrieve the JWT token from the Authorization header
        authorization_header = request.headers.get('Authorization')

        if not authorization_header or not authorization_header.startswith('Bearer '):
            raise AuthenticationFailed('Invalid or missing Bearer token!')

        token = authorization_header.split('Bearer ')[1].strip()  # Strip whitespaces

        try:
            # Make sure to use the same secret key that was used to encode the JWT
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('JWT has expired!')
        except jwt.DecodeError:
            raise AuthenticationFailed('JWT is invalid!')

        user = User.objects.filter(id=payload['id']).first()

        if not user:
            raise AuthenticationFailed('User not found!')

        profile =  Profilecomplete1.objects.filter(user=user).all()

        if not profile:
            raise AuthenticationFailed('Profile not found!')

        # You should import and use your profile serializer here
        serializer = Profilecomplete1Serializer(profile,many=True)

        return Response(serializer.data)   
    








class Profilecomplete2ListCreateView(views.APIView):

    def post(self, request):
        # Ensure that the user does not already have a profile

        authorization_header = request.headers.get('Authorization')

        if not authorization_header or not authorization_header.startswith('Bearer '):
            raise AuthenticationFailed('Invalid or missing Bearer token!')

        token = authorization_header.split('Bearer ')[1]

        if not token:
            raise AuthenticationFailed('Invalid or missing token!')

        try:
            # Make sure to use the same secret key that was used to encode the JWT
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('JWT has expired!')
        except jwt.DecodeError:
            raise AuthenticationFailed('JWT is invalid!')

        user1 = User.objects.filter(id=payload['id']).first()

        profile, created = Profilecomplete2.objects.get_or_create(user=user1)

        if not created:
            # If the profile already exists, update the values
            serializer = Profilecomplete2Serializer(profile, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # If the profile was created (not already existing)
        serializer = Profilecomplete2Serializer(data=request.data)
        if serializer.is_valid():
            # Create a new profile for the authenticated user
            serializer.save(user=user1)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    
    



class viewprofilecomplete2(views.APIView):

    def get(self, request):
        # Retrieve the JWT token from the Authorization header
        authorization_header = request.headers.get('Authorization')

        if not authorization_header or not authorization_header.startswith('Bearer '):
            raise AuthenticationFailed('Invalid or missing Bearer token!')

        token = authorization_header.split('Bearer ')[1].strip()  # Strip whitespaces

        try:
            # Make sure to use the same secret key that was used to encode the JWT
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('JWT has expired!')
        except jwt.DecodeError:
            raise AuthenticationFailed('JWT is invalid!')

        user = User.objects.filter(id=payload['id']).first()

        if not user:
            raise AuthenticationFailed('User not found!')

        profile =  Profilecomplete2.objects.filter(user=user).all()

        if not profile:
            raise AuthenticationFailed('Profile not found!')

        # You should import and use your profile serializer here
        serializer = Profilecomplete2Serializer(profile,many=True)

        return Response(serializer.data)   
    





class Profilecomplete3ListCreateView(views.APIView):

    def post(self, request):
        # Ensure that the user does not already have a profile

        authorization_header = request.headers.get('Authorization')

        if not authorization_header or not authorization_header.startswith('Bearer '):
            raise AuthenticationFailed('Invalid or missing Bearer token!')

        token = authorization_header.split('Bearer ')[1]

        if not token:
            raise AuthenticationFailed('Invalid or missing token!')

        try:
            # Make sure to use the same secret key that was used to encode the JWT
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('JWT has expired!')
        except jwt.DecodeError:
            raise AuthenticationFailed('JWT is invalid!')

        user1 = User.objects.filter(id=payload['id']).first()

        profile, created = Profilecomplete3.objects.get_or_create(user=user1)

        if not created:
            # If the profile already exists, update the values
            serializer = Profilecomplete3Serializer(profile, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # If the profile was created (not already existing)
        serializer = Profilecomplete3Serializer(data=request.data)
        if serializer.is_valid():
            # Create a new profile for the authenticated user
            serializer.save(user=user1)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    
    



class viewprofilecomplete3(views.APIView):

    def get(self, request):
        # Retrieve the JWT token from the Authorization header
        authorization_header = request.headers.get('Authorization')

        if not authorization_header or not authorization_header.startswith('Bearer '):
            raise AuthenticationFailed('Invalid or missing Bearer token!')

        token = authorization_header.split('Bearer ')[1].strip()  # Strip whitespaces

        try:
            # Make sure to use the same secret key that was used to encode the JWT
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('JWT has expired!')
        except jwt.DecodeError:
            raise AuthenticationFailed('JWT is invalid!')

        user = User.objects.filter(id=payload['id']).first()

        if not user:
            raise AuthenticationFailed('User not found!')

        profile =  Profilecomplete3.objects.filter(user=user).all()

        if not profile:
            raise AuthenticationFailed('Profile not found!')

        # You should import and use your profile serializer here
        serializer = Profilecomplete3Serializer(profile,many=True)

        return Response(serializer.data)   
    








class Profilecomplete4ListCreateView(views.APIView):

    def post(self, request):
        # Ensure that the user does not already have a profile

        authorization_header = request.headers.get('Authorization')

        if not authorization_header or not authorization_header.startswith('Bearer '):
            raise AuthenticationFailed('Invalid or missing Bearer token!')

        token = authorization_header.split('Bearer ')[1]

        if not token:
            raise AuthenticationFailed('Invalid or missing token!')

        try:
            # Make sure to use the same secret key that was used to encode the JWT
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('JWT has expired!')
        except jwt.DecodeError:
            raise AuthenticationFailed('JWT is invalid!')

        user1 = User.objects.filter(id=payload['id']).first()

        profile, created = Profilecomplete4.objects.get_or_create(user=user1)

        if not created:
            # If the profile already exists, update the values
            serializer = Profilecomplete4Serializer(profile, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # If the profile was created (not already existing)
        serializer = Profilecomplete4Serializer(data=request.data)
        if serializer.is_valid():
            # Create a new profile for the authenticated user
            serializer.save(user=user1)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    
    



class viewprofilecomplete4(views.APIView):

    def get(self, request):
        # Retrieve the JWT token from the Authorization header
        authorization_header = request.headers.get('Authorization')

        if not authorization_header or not authorization_header.startswith('Bearer '):
            raise AuthenticationFailed('Invalid or missing Bearer token!')

        token = authorization_header.split('Bearer ')[1].strip()  # Strip whitespaces

        try:
            # Make sure to use the same secret key that was used to encode the JWT
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('JWT has expired!')
        except jwt.DecodeError:
            raise AuthenticationFailed('JWT is invalid!')

        user = User.objects.filter(id=payload['id']).first()

        if not user:
            raise AuthenticationFailed('User not found!')

        profile =  Profilecomplete4.objects.filter(user=user).all()

        if not profile:
            raise AuthenticationFailed('Profile not found!')

        # You should import and use your profile serializer here
        serializer = Profilecomplete4Serializer(profile,many=True)

        return Response(serializer.data)  
    





class Profilecomplete5ListCreateView(views.APIView):

    def post(self, request):
        # Ensure that the user does not already have a profile

        authorization_header = request.headers.get('Authorization')

        if not authorization_header or not authorization_header.startswith('Bearer '):
            raise AuthenticationFailed('Invalid or missing Bearer token!')

        token = authorization_header.split('Bearer ')[1]

        if not token:
            raise AuthenticationFailed('Invalid or missing token!')

        try:
            # Make sure to use the same secret key that was used to encode the JWT
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('JWT has expired!')
        except jwt.DecodeError:
            raise AuthenticationFailed('JWT is invalid!')

        user1 = User.objects.filter(id=payload['id']).first()

        profile, created = Profilecomplete5.objects.get_or_create(user=user1)

        if not created:
            # If the profile already exists, update the values
            serializer = Profilecomplete5Serializer(profile, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # If the profile was created (not already existing)
        serializer = Profilecomplete5Serializer(data=request.data)
        if serializer.is_valid():
            # Create a new profile for the authenticated user
            serializer.save(user=user1)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    
    



class viewprofilecomplete5(views.APIView):

    def get(self, request):
        # Retrieve the JWT token from the Authorization header
        authorization_header = request.headers.get('Authorization')

        if not authorization_header or not authorization_header.startswith('Bearer '):
            raise AuthenticationFailed('Invalid or missing Bearer token!')

        token = authorization_header.split('Bearer ')[1].strip()  # Strip whitespaces

        try:
            # Make sure to use the same secret key that was used to encode the JWT
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('JWT has expired!')
        except jwt.DecodeError:
            raise AuthenticationFailed('JWT is invalid!')

        user = User.objects.filter(id=payload['id']).first()

        if not user:
            raise AuthenticationFailed('User not found!')

        profile =  Profilecomplete5.objects.filter(user=user).all()

        if not profile:
            raise AuthenticationFailed('Profile not found!')

        # You should import and use your profile serializer here
        serializer = Profilecomplete5Serializer(profile,many=True)

        return Response(serializer.data)  

    


    
    



    
    




