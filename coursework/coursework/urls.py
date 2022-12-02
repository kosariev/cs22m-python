from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('cars/', views.cars),
    path('add', views.add),
    path('edit/<int:car_id>', views.edit),
    path('update/<int:car_id>', views.update),
    path('delete/<int:car_id>', views.destroy),
    path('admin/', admin.site.urls),
]
