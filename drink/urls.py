from django.urls import path
from drink import views

app_name = 'drink'

urlpatterns = [
	path('<type>/<drink_name>/', views.get_item_by_name, name='get_item_by_name'),
]

