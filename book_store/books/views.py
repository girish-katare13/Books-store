from django.shortcuts import render
from rest_framework import generics, status
from .models import Book
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.

# Custom TokenObtainPairView for JWT authentication
class CustomTokenObtainPairView(TokenObtainPairView):
    pass

# This view handles the listing and creation of Book objects.
class BookListCreate(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]  # Authenticate users with JWT tokens
    permission_classes = [IsAuthenticated]  # Ensure that only authenticated users can access this view
    queryset = Book.objects.all()  # Retrieve all Book objects from the database
    serializer_class = BookSerializer  # Use the BookSerializer to serialize/deserialize the data

    # Handle the HTTP POST request for creating a new Book object.
    def post(self, request, *args, **kwargs):
        # Initialize the serializer with the incoming request data.
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Save the validated data and return a success response.
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Return an error response if the data is invalid.
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# This view handles the retrieval, updating, and deletion of Book objects.
class BookRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]  # Authenticate users with JWT tokens
    permission_classes = [IsAuthenticated]  # Ensure that only authenticated users can access this view
    queryset = Book.objects.all()  # Retrieve all Book objects from the database
    serializer_class = BookSerializer  # Use the BookSerializer to serialize/deserialize the data

    # Handle the HTTP PUT request for updating an existing Book object.
    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        # Validate and update the serializer with the incoming data.
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            # Perform the update and return the updated data.
            self.perform_update(serializer)
            return Response(serializer.data)
        # Return an error response if the data is invalid.
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handle the HTTP DELETE request for deleting an existing Book object.
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        # Perform the deletion of the specified Book object.
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
