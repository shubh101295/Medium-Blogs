from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Q 

from .models import Restaurant, Item

@api_view(["POST"])
def createRestaurant(request):
	try:
		name = request.data["name"]
		address = request.data["address"]
		restaurant = Restaurant(name=name , address =address)
		restaurant.save()
		return Response("Restaurant Created" , status=status.HTTP_200_OK)	
	except:
		return Response("Some Error Occurred" , status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def restaurantList(request):
	restaurants = Restaurant.objects.all().values()
	return Response(restaurants, status=status.HTTP_200_OK)		

@api_view(["DELETE"])
def deleteRestaurant(request, id):
	restaurant = Restaurant.objects.filter(Q(id=id))
	if len(restaurant)>0:
		restaurant[0].delete()
		return Response("Restaurant deleted", status=status.HTTP_200_OK)
	else:
		return Response("No restaurant with the id found",status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST","PUT", "DELETE"])
def itemAPI(request):
	## first find whether the resaurant with the given id exists or not
	try:
		restaurant = Restaurant.objects.filter(id=request.data["restaurant_id"])
		if len(restaurant)==0:
			return Response("NO restaurant with the given id found", status=status.HTTP_400_BAD_REQUEST)
	except:
		return Response("Restaurant id not correct", status=status.HTTP_400_BAD_REQUEST)
	if request.method == "POST":
		item = Item(name= request.data["name"], cost=request.data["cost"], restaurant=restaurant[0])
		item.save()
		return Response("Item added to restaurant",status=status.HTTP_200_OK)
	elif request.method == "PUT":
		try:
			items = Item.objects.filter(Q(id=request.data["item_id"]) & Q(restaurant=request.data["restaurant_id"]))
			if len(items)==0:
				return Response("No items with the given id found in the restaurant", status=status.HTTP_400_BAD_REQUEST)
		except:
			return Response("id's are not correct", status=status.HTTP_400_BAD_REQUEST)
		item = items[0]
		# here I have implemented logic to change the cost of an item , but you can always modify it to edit anything you want
		item.cost = request.data["cost"]
		item.save()
		return Response("Item cost edited", status=status.HTTP_200_OK)

