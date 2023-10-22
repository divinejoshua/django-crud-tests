from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('list', views.BlogList.as_view()),
    path('create', views.CreateBlog.as_view()),
    path('<int:blogId>', views.BlogDetail.as_view()),
]