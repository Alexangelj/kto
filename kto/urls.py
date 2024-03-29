from django.urls import path
from . import views
from django.contrib import admin

app_name = 'kto'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:task_id>/delete/', views.delete_task, name='delete'),
    path('add/', views.add_task, name='add'),
    path('<int:task_id>/complete', views.complete, name='complete'),
    path('<int:task_id>/edit', views.set_time, name='set_time'),
]