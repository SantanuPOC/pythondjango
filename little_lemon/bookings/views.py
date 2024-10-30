from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Menu, TableBooking
from .serializers import MenuSerializer, TableBookingSerializer

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class TableBookingViewSet(viewsets.ModelViewSet):
    queryset = TableBooking.objects.all()
    serializer_class = TableBookingSerializer

def index(request):
    return render(request, 'index.html')