#define URL route for index() view
from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('menu-items', views.MenuViewSet, basename='menu-items')
router.register('bookings', views.BookingViewSet, basename='bookings')
router.register("users", views.UserViewSet, basename="user")


urlpatterns = [
    path("", include(router.urls)),
    path("home/", views.index, name='home'),
    path("api-token-auth/", obtain_auth_token),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
