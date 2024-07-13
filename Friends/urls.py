from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import FriendsOperationsView


router = SimpleRouter()
router.register(r'friends', FriendsOperationsView, basename='friends')


urlpatterns = [
    path('api/v8/', include(router.urls)) # api/v8/friends/...
]