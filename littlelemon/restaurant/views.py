from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer, UserSerializer
from .permissions import IsManager


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser | IsManager]
        return [permission() for permission in permission_classes]


class BookingViewSet(viewsets.ModelViewSet):
    booking = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        if self.request.method not in ["GET", "POST"]:
            permission_classes = [IsAdminUser | IsManager]
        return [permission() for permission in permission_classes]


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer
