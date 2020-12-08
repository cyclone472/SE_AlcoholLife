from django.urls import path
from drink import views

app_name = 'drink'

urlpatterns = [
	path('add/', views.add_category, name='add_category'),
	path('addrink/', views.add_drink, name='add_drink'),
	path('addrating/', views.add_rating, name='add_rating'),
	path('<drink_name>/', views.get_item_by_name, name='get_item_by_name'),
	path('items/<category>/', views.get_items, name='get_items'),
	path('<drink_name>/reviews', views.get_reviews_for_drink, name='get_reviews_for_drink'),
	path('review/<int:review_id>', views.get_review, name='get_review')
]

