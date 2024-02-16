from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter

# urls.py
from django.urls import path
from .views import UserDetailsViewSet


# urlpatterns = [
#     path('all/', UserDetailsViewSet.as_view({'get': 'list'}), name='user_infor'),
# ]


router = DefaultRouter()
router.register(r'all', UserDetailsViewSet, basename='user_info')

urlpatterns = [
    path('', include(router.urls)),
]