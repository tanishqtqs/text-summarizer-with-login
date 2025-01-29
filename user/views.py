from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

# Get the custom user model
User = get_user_model()

class PingView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({"message": "User app is working!"}, status=200)

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        age = request.data.get('age')
        gender = request.data.get('gender')

        # Validate input
        if not username or not password or not email:
            return Response(
                {"error": "Username, password, and email are required."}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        if User.objects.filter(username=username).exists():
            return Response(
                {"error": "Username already exists."}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        if User.objects.filter(email=email).exists():
            return Response(
                {"error": "Email already registered."}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        # Create the user
        user = User.objects.create_user(
            username=username, 
            password=password, 
            email=email, 
            first_name=first_name, 
            last_name=last_name
        )
        user.age = age
        user.gender = gender
        user.save()

        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)

        return Response({
            "message": "User registered successfully.",
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)
