from .models import Post
from .serializers import PostSerializer
from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated


class PostViewSet(viewsets.ModelViewSet):
    model = Post
    queryset = Post.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer
