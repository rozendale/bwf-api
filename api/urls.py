from django.urls import include
from api import views
from rest_framework import routers
from django.urls import re_path

router = routers.DefaultRouter()
router.register(r'groups', views.GroupViewset)
router.register(r'events', views.EventViewset)
router.register(r'members', views.MemberViewset)
router.register(r'users', views.UserViewset)
router.register(r'profile', views.UserProfileViewset)

urlpatterns = [
    re_path(r'^', include(router.urls)),
    re_path('authenticate/', views.CustomObtainAuthToken.as_view()),
]