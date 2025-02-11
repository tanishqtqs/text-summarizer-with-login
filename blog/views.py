from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from .models import Blog
from .serializers import BlogSerializer
from aiml.summarizer import summarize_text

class PingView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({"message": "Blog app is working!"}, status=200)

class CreateBlogView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can create blogs

    def post(self, request):
        original_content = request.data.get('content')
        if not original_content:
            return Response({"error": "Blog content is required."}, status=status.HTTP_400_BAD_REQUEST)

        # Summarize the content using the external function
        summarized_content = summarize_text(original_content)

        # Create the blog entry in the database
        blog = Blog.objects.create(
            user=request.user,
            original_content=original_content,
            summarized_content=summarized_content
        )

        return Response({
            "message": "Blog created successfully.",
            "summarized_content": summarized_content,
            "blog_id": blog.id
        }, status=status.HTTP_201_CREATED)


class UserBlogsView(APIView):
    permission_classes = [IsAuthenticated]  # Only authenticated users can access their blogs

    def get(self, request):
        user_blogs = Blog.objects.filter(user=request.user)
        
        if not user_blogs.exists():
            return Response({"message": "No blogs found for this user."}, status=status.HTTP_404_NOT_FOUND)

        serializer = BlogSerializer(user_blogs, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)