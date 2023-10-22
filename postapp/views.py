from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class BlogList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        context = {}
        context['message'] = True
        # snippets = Snippet.objects.all()
        # serializer = SnippetSerializer(snippets, many=True)
        return Response(context,  status=status.HTTP_200_OK)

    # def post(self, request, format=None):
    #     serializer = SnippetSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateBlog(APIView):
    """
    Create a new blog
    """
    def post(self, request, format=None):
        context = {}
        context['message'] = True
        return Response(context,  status=status.HTTP_200_OK)


class BlogDetail(APIView):
    """
    Blog detail
    """
    def get(self, request, format=None):
        context = {}
        context['message'] = "GET blog post"
        return Response(context,  status=status.HTTP_200_OK)

    def put(self, request, format=None):
        context = {}
        context['message'] = "UPDATE blog post"
        return Response(context,  status=status.HTTP_200_OK)

    def delete(self, request, format=None):
        context = {}
        context['message'] = "DELETE blog post"
        return Response(context,  status=status.HTTP_200_OK)