from ApiApp.models import Blog
from .serializer import Blogserializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

# class BlogViewSets(viewsets.ViewSet):
#
#     def list(self, request, *args, **kwargs):
#         queryset = Blog.objects.all()
#         serializer = Blogserializer(queryset, many=True)
#         return Response(serializer.data)


class BlogViewSets(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = Blogserializer

    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('created_at').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)