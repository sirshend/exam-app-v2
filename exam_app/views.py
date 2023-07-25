from django.shortcuts import render
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer, UserLoginSerializer

@api_view(['POST'])
def register_user(request):
    serializer = UserRegistrationSerializer(data=request.data)
    return Response({'message': 'User registered successfully'})
    # if serializer.is_valid():
    #     # Perform registration logic here (create user, generate private key, store in DB)
    #     # use PyECDSA here to generate private keys
    #     # Store user details in the database
    #     # Return a success response
    #     return Response({'message': 'User registered successfully'})
    # else:
    #     # Return validation error response
    #     return Response(serializer.errors, status=400)

@api_view(['POST'])
def login_user(request):
    serializer = UserLoginSerializer(data=request.data)
    return Response({'message': 'User login successfully'})
    # if serializer.is_valid():
    #     # Perform login logic here (verify credentials, generate access token, etc.)
    #     # Return a success response with the access token
    #     return Response({'message': 'User logged in successfully', 'access_token': 'your_access_token'})
    # else:
    #     # Return validation error response
    #     return Response(serializer.errors, status=400)
