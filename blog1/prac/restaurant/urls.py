from django.urls import path,include

from .views import createRestaurant,restaurantList,deleteRestaurant,itemAPI

urlpatterns = [
	path('create/',createRestaurant, name="createRestaurant"),
	path('all/',restaurantList, name="restaurantList"),
	path('delete/<int:id>/',deleteRestaurant, name="deleteRestaurant"),
	path('item/',itemAPI, name="itemAPI"),
]