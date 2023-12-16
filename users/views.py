from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import login, logout, authenticate
from django.db import transaction
from .serializers import UserSerializer

# Create your views here.
class SignupView(APIView):
    @transaction.atomic
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Signup successful"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    @transaction.atomic
    def post(self, request):
        if request.user.is_authenticated:
            return Response({"error":"User is already logged-in"}, status=status.HTTP_400_BAD_REQUEST)
        username = request.data.get("username")
        password = request.data.get("password")
        
        user = authenticate(username=username, password=password)
        if not user:
            return Response({"error":"error!"}, status=status.HTTP_400_BAD_REQUEST)
        login(request=request, user=user)
        return Response({"message":"login successful"}, status=status.HTTP_200_OK)

class LogoutView(APIView):
    @transaction.atomic
    def post(self, request):
        logout(request=request)
        return Response({"message":"logout successful"}, status=status.HTTP_200_OK)

class UserInfoView(APIView):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            return Response({"message": f"{user.username} is logged in"})
        return Response({"message": "Session expired or not found"}, status=status.HTTP_404_NOT_FOUND)
    
    @transaction.atomic
    def delete(self, request):
        user = request.user
        if user.is_authenticated:
            user.delete()
            return Response({"message": "User is unregistered successfully"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "User has no authorization"}, status=status.HTTP_401_UNAUTHORIZED)
    