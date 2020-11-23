from django.urls import path
from drink import views

app_name = 'drink'

urlpatterns = [
	path('add/', views.add_category, name='add_category'),
	path('addrink/', views.add_drink, name='add_drink'),
	path('<drink_name>/', views.get_item_by_name, name='get_item_by_name'),
]

