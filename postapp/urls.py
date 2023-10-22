from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('blog/list', views.BlogList.as_view()),
    path('blog/create', views.CreateBlog.as_view()),
    path('blog/<int:blogId>', views.BlogDetail.as_view()),
]