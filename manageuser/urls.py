from django.urls import path
from manageuser import views

app_name = 'manageuser'

urlpatterns = [
    path('user/', views.manage_user, name='manage_user'), # POST, PUT request
	path('review/', views.create_review, name='create_review'),
	path('comment/', views.create_comment, name='create_comment'),
	path('reviews/', views.get_review_for_drink, name='get_review_for_drink'),
	path('login/', views.login, name='login'),
	path('logout/', views.logout, name='logout')
]
