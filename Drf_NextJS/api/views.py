from rest_framework import generics
from .models import Posts
from .serializers import PostSerializer
from .pagination import TestingOffsetPagination


class PostView(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Posts.objects.all().order_by('-date_created')
    serializer_class = PostSerializer
    # pagination_class = TestingOffsetPagination


class PostListAPIView(generics.RetrieveAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'
