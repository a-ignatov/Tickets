from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main),
    path('change_status/<pk>/', views.TicketChangeView.as_view()),
]
