from django.urls import path
from main.views import TaskList
from .import  views


urlpatterns = [
    path("", TaskList.as_view(), name='task_list'),
    path("funçao/", views.task_list, name= 'task_list_funçao'), #Essa função só é ativada quando o caminhoda URL é escrito. 
    path("concluidas/", views.task_concluido, name= 'concluidas')

]
