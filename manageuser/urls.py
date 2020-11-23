from django.urls import path
from manageuser import views

app_name = 'manageuser'

urlpatterns = [
    path('user/', views.manage_user, name='manage_user'), # POST, PUT request
]
