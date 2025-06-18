from django.urls import path,include
from .views import post_list,admin_view,user_view
from django.contrib.auth import views as auth_views

urlpatterns = [        
    path('', post_list, name='post_list'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', admin_view, name='admin_view'),
    path('user/', user_view, name='user_view'),
]