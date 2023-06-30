from django.contrib import admin
from django.urls import include, path

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('change_status/<pk>/', views.ticket_update, name='ticket_change_status'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

]

