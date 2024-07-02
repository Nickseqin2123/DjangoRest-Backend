from django.urls import path, include, re_path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView, TokenRefreshView
from rest_framework_simplejwt.views import TokenBlacklistView


urlpatterns = [
    path('api/v8/users/', Users.as_view()),
    path('api/v8/user/<int:pk>/', UserOther.as_view()),
    
    path('api/v8/registration/', include('djoser.urls')),
    re_path('api/v8/auth/', include('djoser.urls')), # api/v8/auth/users/me - профиль и можно многое другое см. Документация
    
    path('api/v8/token/logout/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('api/v8/token/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    path('api/v8/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/v8/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  
]

# PATCH запрос изменяет не все, а только часть (при запросе на изменения профиля)