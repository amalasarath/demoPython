from django.contrib import admin
from django.urls import path
from . import views
app_name="todoapp"
urlpatterns = [
    path('',views.todo,name='todo'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('chome/',views.TaskListview.as_view(),name='chome'),
    path('cdetail/<int:pk>/',views.TaskDetailview.as_view(),name='cdetail'),
    path('cupdate/<int:pk>/',views.TaskUpdateview.as_view(),name='cupdate'),
    path('cdelete/<int:pk>/',views.TaskDeleteview.as_view(),name='cdelete'),
]
