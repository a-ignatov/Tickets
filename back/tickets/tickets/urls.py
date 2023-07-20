from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import LogoutView, LoginView

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('change_status/<pk>/', views.ticket_update, name='ticket_change_status'),
    path('create', views.ticket_create, name='ticket_create'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path(
        'login/',
        LoginView.as_view
        (template_name='users/login.html'),
        name='login'
    ),
]

