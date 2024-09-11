from django.urls import path, include
from rest_framework.routers import SimpleRouter 

from .views import UserViewSet, PostViewSet 


router = SimpleRouter()
router.register('users', UserViewSet, base_name='users')
router.register('', PostViewSet, base_name='posts')

urlpatterns = [
    path('', include(router.urls))
]