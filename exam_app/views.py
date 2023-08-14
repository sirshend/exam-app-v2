import jwt
from django.shortcuts import render
# Create your views here.
from datetime import datetime, timedelta
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer, UserLoginSerializer, ExamSerializer, StudentSerializer, ProfessorSerializer
from .models import UserRegistration, UserLogin, Exam, Student, Professor
from .models import Exam, Student, Professor, UserRegistration, UserLogin
from ecdsa import SigningKey, SECP256k1

@api_view(['POST'])
def register_user(request):
    serializer = UserRegistrationSerializer(data=request.data)
    #return Response({'message': 'User registered successfully'})
    # if serializer.is_valid():
    #     # Perform registration logic here (create user, generate private key, store in DB)
    #     # use PyECDSA here to generate private keys
    #     # Store user details in the database
    #     # Return a success response
    #     return Response({'message': 'User registered successfully'})
    # else:
    #     # Return validation error response
    #     return Response(serializer.errors, status=400)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        password = serializer.validated_data['password']
        role = serializer.validated_data['role']

        # Check if user already exists
        if UserRegistration.objects(name=name).first():
            return Response({'message': 'User already exists'})

        # Generate and store keys using your ecdsa signer code (to be added later)
        # For now, just assume some dummy keys are generated
        # public_key = "dummy_public_key"
        # private_key = "dummy_private_key"
        private_key = SigningKey.generate(curve=SECP256k1)
        private_key_hex = private_key.to_string().hex()

        # Store the user details in the database
        # user = UserRegistration(name=name, password=password, role=role, public_key=public_key, private_key=private_key)
        # user.save()
        user_registration = UserRegistration(name=name, password=password, role=role, private_key=private_key_hex)
        user_registration.save()
        # Return the response with the keys
        return Response({
            'message': 'User registered successfully',
            'private_key': private_key_hex
        })
    else:
        # Return validation error response
        return Response(serializer.errors, status=400)
@api_view(['POST'])
def login_user(request):
    serializer = UserLoginSerializer(data=request.data)
    #return Response({'message': 'User login successfully'})
    # if serializer.is_valid():
    #     # Perform login logic here (verify credentials, generate access token, etc.)
    #     # Return a success response with the access token
    #     return Response({'message': 'User logged in successfully', 'access_token': 'your_access_token'})
    # else:
    #     # Return validation error response
    #     return Response(serializer.errors, status=400)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        password = serializer.validated_data['password']

        # Check if user exists and password is correct
        user = UserRegistration.objects(name=name).first()
        if not user:
            return Response({'message': 'User not registered'})

        if user.password != password:
            return Response({'message': 'Password incorrect'})

        # Generate JWT token
        # token = jwt.encode({
        #     'name': name,
        #     'exp': datetime.utcnow() + timedelta(minutes=settings.JWT_EXPIRATION_DELTA)
        # }, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)

        # Generate JWT token
        token = jwt.encode({
            'name': name,
            'exp': datetime.utcnow() + settings.JWT_EXPIRATION_DELTA
        }, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)

        # Update the user's token in the database
        user_login = UserLogin.objects(name=name).first()
        if not user_login:
            user_login = UserLogin(name=name)
        user_login.token = token
        user_login.save()

        # Return the response with the token
        return Response({
            'message': 'User login successfully',
            'token': token
        })
    else:
        # Return validation error response
        return Response(serializer.errors, status=400)


@api_view(['POST'])
def apply_for_exam(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        token = serializer.validated_data['token']

        # Check if user exists and token is valid
        user_login = UserLogin.objects(name=name).first()
        if not user_login:
            return Response({'message': 'User not registered'})

        try:
            decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
            if decoded_token['name'] != name:
                raise jwt.DecodeError
            if datetime.fromtimestamp(decoded_token['exp']) < datetime.utcnow():
                raise jwt.ExpiredSignatureError
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Session has ended. Do a fresh login'})
        except jwt.DecodeError:
            return Response({'message': 'Invalid token'})

        # Check if the user has the role 'student'
        user = Student.objects(name=name).first()
        if not user:
            return Response({'message': 'Only students can apply for the exam'})

        # Get the list of professors' names from the request data
        professors = request.data.get('professors', [])
        if not isinstance(professors, list):
            return Response({'message': 'Invalid professors data format'})

        # Check if the professors' names exist in the database
        existing_professors = Professor.objects(name__in=professors)
        if len(existing_professors) != len(professors):
            return Response({'message': 'Some professors do not exist in the database'})

        # Add professors to the student's 'partners' field
        user.partners = professors
        user.save()

        # Add the student's name to the professors' 'permissions_pending' field
        for professor in existing_professors:
            professor.permissions_pending.append(name)
            professor.save()

        # Return the response
        return Response({'message': 'Application for exam submitted successfully'})
    else:
        # Return validation error response
        return Response(serializer.errors, status=400)


@api_view(['POST'])
def approve_requests(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        token = serializer.validated_data['token']

        # Check if user exists and token is valid
        user_login = UserLogin.objects(name=name).first()
        if not user_login:
            return Response({'message': 'User not registered'})

        try:
            decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
            if decoded_token['name'] != name:
                raise jwt.DecodeError
            if datetime.fromtimestamp(decoded_token['exp']) < datetime.utcnow():
                raise jwt.ExpiredSignatureError
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Session has ended. Do a fresh login'})
        except jwt.DecodeError:
            return Response({'message': 'Invalid token'})

        # Check if the user has the role 'professor'
        user = Professor.objects(name=name).first()
        if not user:
            return Response({'message': 'Only professors can approve requests for exams'})

        # Get the list of student names from the request data
        students = request.data.get('students', [])
        if not isinstance(students, list):
            return Response({'message': 'Invalid students data format'})

        # Check if the student names exist in the database
        existing_students = Student.objects(name__in=students)
        if len(existing_students) != len(students):
            return Response({'message': 'Some students do not exist in the database'})

        # Process each student and update their 'permissions_obtained' field
        for student in existing_students:
            if name in student.partners:
                student.partners.remove(name)  # Remove professor from student's 'partners' list
                student.permissions_obtained.append(name)  # Add professor to student's 'permissions_obtained' list
                student.save()

        # Return the response
        return Response({'message': 'Requests approved successfully'})
    else:
        # Return validation error response
        return Response(serializer.errors, status=400)

@api_view(['POST'])
def check_status(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        token = serializer.validated_data['token']

        # Check if user exists and token is valid
        user_login = UserLogin.objects(name=name).first()
        if not user_login:
            return Response({'message': 'User not registered'})

        try:
            decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
            if decoded_token['name'] != name:
                raise jwt.DecodeError
            if datetime.fromtimestamp(decoded_token['exp']) < datetime.utcnow():
                raise jwt.ExpiredSignatureError
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Session has ended. Do a fresh login'})
        except jwt.DecodeError:
            return Response({'message': 'Invalid token'})

        # Check if the user has the role 'student'
        user = Student.objects(name=name).first()
        if not user:
            return Response({'message': 'Only students can check status for the applied exam'})

        # Check if 'partners' field is blank
        if not user.partners:
            return Response({'message': 'User has not applied for an exam'})

        # Check if all partners are present in 'permissions_obtained' field
        missing_permissions = [partner for partner in user.partners if partner not in user.permissions_obtained]
        if missing_permissions:
            return Response({'message': 'Some permissions are pending', 'missing_permissions': missing_permissions})
        else:
            return Response({'message': 'All professors approved. You can sit for the exam'})
    else:
        # Return validation error response
        return Response(serializer.errors, status=400)