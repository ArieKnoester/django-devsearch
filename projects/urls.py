from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_projects_page, name='all-projects-page'),
    path('project-page/<str:pk>', views.project_page, name='project-page'),
    path('create-project/', views.create_project, name='create-project'),
    path('update-project/<str:pk>', views.update_project, name='update-project'),
    path('delete-project/<str:pk>', views.delete_project, name='delete-project')
]
