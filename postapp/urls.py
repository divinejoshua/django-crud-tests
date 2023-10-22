from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('bloglist/', views.BlogList.as_view()),
    # path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]