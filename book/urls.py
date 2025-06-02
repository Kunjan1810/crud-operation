from django.urls import path
from .views import BookAPIView

urlpatterns = [
    path('', BookAPIView.as_view(), name='book_list'),           #
    path('<int:pk>/', BookAPIView.as_view(), name='book_detail'),  # GET/PUT/DELETE one
]
