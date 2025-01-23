# Create your views here.
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

class PingView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({"message": "User app is working!"}, status=200)
