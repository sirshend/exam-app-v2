# from rest_framework_mongoengine import serializers
# from .models import Student, Professor, Exam

# class StudentSerializer(serializers.DocumentSerializer):
#     class Meta:
#         model = Student
#         fields = '__all__'

# class ProfessorSerializer(serializers.DocumentSerializer):
#     class Meta:
#         model = Professor
#         fields = '__all__'

# class ExamSerializer(serializers.DocumentSerializer):
#     class Meta:
#         model = Exam
#         fields = '__all__'
        
# class UserRegistrationSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=255)
#     email = serializers.EmailField()
#     registration_number = serializers.CharField(max_length=50)
#     role = serializers.CharField(max_length=50)
#     password = serializers.CharField(max_length=255)

# class UserLoginSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField(max_length=255)

from rest_framework_mongoengine import serializers
from .models import Exam, Student, Professor, UserRegistration, UserLogin


class ExamSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Exam
        fields = '__all__'


class StudentSerializer(serializers.DocumentSerializer):
    applied_exams = ExamSerializer(many=True)
    permissions_received = ExamSerializer(many=True)
    permissions_pending = ExamSerializer(many=True)

    class Meta:
        model = Student
        exclude = ('password', 'private_key',)


class ProfessorSerializer(serializers.DocumentSerializer):
    validate_requests = ExamSerializer(many=True)

    class Meta:
        model = Professor
        exclude = ('password', 'private_key',)

# class UserRegistrationSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=255)
#     email = serializers.EmailField()
#     registration_number = serializers.CharField(max_length=50)
#     role = serializers.CharField(max_length=50)
#     password = serializers.CharField(max_length=255)

# class UserLoginSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField(max_length=255)
class UserRegistrationSerializer(serializers.DocumentSerializer):
    class Meta:
        model = UserRegistration
        fields = '__all__'

class UserLoginSerializer(serializers.DocumentSerializer):
    class Meta:
        model = UserLogin
        fields = '__all__'