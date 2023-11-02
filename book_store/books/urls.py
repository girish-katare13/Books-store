from django.urls import path
from .views import BookListCreate,BookRetrieveUpdateDestroy
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # API endpoint for listing and creating books.
    path('api/books/', BookListCreate.as_view(), name='book-list-create'),
    # API endpoint for retrieving, updating, and deleting specific books.
    path('api/books/<int:pk>/', BookRetrieveUpdateDestroy.as_view(), name='book-retrieve-update-destroy'),
    # API endpoint for obtaining a JWT token.
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
