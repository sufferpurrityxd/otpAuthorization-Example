from .routers import router
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('otp/', include(router.urls)),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh', TokenRefreshView.as_view()),
]


