from django.urls import path
from .views import register_user, login_user, apply_for_exam, approve_requests, check_status

urlpatterns = [
    # path('register/', register_user, name='register'),
    # path('login/', login_user, name='login'),
    # Add more API URLs as needed
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('apply-for-exam/', apply_for_exam, name='apply-for-exam'),
    path('approve-requests/', approve_requests, name='approve-requests'),
    path('check-status/', check_status, name='check-status'),
]
