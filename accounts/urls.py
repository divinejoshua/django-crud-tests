from django.urls import path, include
from . import views

app_name = "accounts_api"

urlpatterns = [
    path('user', views.user_view.as_view(), name='get_user'),                       #Check user api
    path('register', views.register_view.as_view(), name='register_user'),              #Register User
    path('auth/', include('dj_rest_auth.urls', namespace='djrest_api')),                #dj rest auth login, change password etc
]