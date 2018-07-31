from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView

from restaurants.models import Restaurant

from .serializers import RestaurantDetailSerializer, RestaurantListSerializer, RestaurantUpdateSerializer


class RestaurantListView(ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantListSerializer


class RestaurantDetailView(RetrieveAPIView):
    serializer_class = RestaurantDetailSerializer
    queryset = Restaurant.objects.all()

class RestaurantUpdateView(RetrieveUpdateAPIView):
	serializer_class = RestaurantUpdateSerializer
	queryset = Restaurant.objects.all()

class RestaurantDeleteView(DestroyAPIView):
	queryset = Restaurant.objects.all()
