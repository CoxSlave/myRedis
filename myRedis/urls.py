from django.contrib import admin
from django.urls import path
from app01 import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home.as_view()),
]
