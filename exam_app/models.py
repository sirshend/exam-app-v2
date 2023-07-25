# from django.db import models

# # Create your models here.

# class Student(models.Model):
#     name = models.CharField(max_length=255)
#     email = models.EmailField(unique=True)
#     registration_number = models.CharField(max_length=50)
#     role = models.CharField(max_length=50)
#     password = models.CharField(max_length=255)
#     private_key = models.CharField(max_length=255)
#     applied_exams = models.ManyToManyField('Exam', related_name='applicants', blank=True)
#     permissions_received = models.ManyToManyField('Exam', related_name='permissions', blank=True)
#     permissions_pending = models.ManyToManyField('Exam', related_name='pending_permissions', blank=True)

#     def __str__(self):
#         return self.name

# class Professor(models.Model):
#     name = models.CharField(max_length=255)
#     email = models.EmailField(unique=True)
#     registration_number = models.CharField(max_length=50)
#     role = models.CharField(max_length=50)
#     password = models.CharField(max_length=255)
#     private_key = models.CharField(max_length=255)
#     validate_requests = models.ManyToManyField('Exam', related_name='validation_requests', blank=True)

#     def __str__(self):
#         return self.name

# class Exam(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name

# class UserRegistrationSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=255)
#     email = serializers.EmailField()
#     registration_number = serializers.CharField(max_length=50)
#     role = serializers.CharField(max_length=50)
#     password = serializers.CharField(max_length=255)

# class UserLoginSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField(max_length=255)

import mongoengine
from mongoengine import Document, StringField, ReferenceField, ListField, EmailField

class Exam(Document):
    name = StringField(max_length=255)

    def __str__(self):
        return self.name

class Student(Document):
    name = StringField(max_length=255)
    email = EmailField(unique=True)
    registration_number = StringField(max_length=50)
    role = StringField(max_length=50)
    password = StringField(max_length=255)
    private_key = StringField(max_length=255)
    applied_exams = ListField(ReferenceField('Exam', reverse_delete_rule=mongoengine.PULL), blank=True)
    permissions_received = ListField(ReferenceField('Exam', reverse_delete_rule=mongoengine.PULL), blank=True)
    permissions_pending = ListField(ReferenceField('Exam', reverse_delete_rule=mongoengine.PULL), blank=True)

    def __str__(self):
        return self.name

class Professor(Document):
    name = StringField(max_length=255)
    email = EmailField(unique=True)
    registration_number = StringField(max_length=50)
    role = StringField(max_length=50)
    password = StringField(max_length=255)
    private_key = StringField(max_length=255)
    validate_requests = ListField(ReferenceField('Exam', reverse_delete_rule=mongoengine.PULL), blank=True)

    def __str__(self):
        return self.name

class UserRegistration(Document):
    name = StringField(max_length=255)
    email = EmailField()
    registration_number = StringField(max_length=50)
    role = StringField(max_length=50)
    password = StringField(max_length=255)

class UserLogin(Document):
    email = EmailField()
    password = StringField(max_length=255)


