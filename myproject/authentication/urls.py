from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from authentication.views import RegisterView, ProtectedView, UserProfileView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    # path('protected/', ProtectedView.as_view(), name='protected'),
    path('profile/', UserProfileView.as_view(), name='profile'),

]