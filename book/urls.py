from django.urls import path
from .views import BookAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', BookAPIView.as_view(), name='book_list'),       
    path('<int:pk>/', BookAPIView.as_view(), name='book_detail'),
]
