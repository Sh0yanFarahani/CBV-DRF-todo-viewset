
from django.urls import path, include
from . import views

app_name = 'task'

urlpatterns = [
    path('', views.TaskList.as_view(), name='task-list'),
    path('task/add', views.TaskCreate.as_view(), name='create-task'),
    path('delete/<int:pk>', views.TaskDelete.as_view(), name='delete-task'),
    path('complete/<int:pk>', views.TaskComplete.as_view(), name='complete-task'),
    path('update/<int:pk>', views.TaskUpdate.as_view(), name='update-task')

]