from django.shortcuts import render
from . import models
from articles.models import Article
from rest_framework.response import Response
from articles.serializers import ArticleSerializer
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['GET', 'POST'])
def index(request):
    articles = Article.objects.all()
    article = articles[0]
    serializer = ArticleSerializer(article)
    
    return Response(serializer.data)