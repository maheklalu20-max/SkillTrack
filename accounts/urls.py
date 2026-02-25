from django.urls import path
from . import views
from . import api_views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('delete-skill/<int:skill_id>/', views.delete_skill, name='delete_skill'),
    path('profile/', views.profile, name='profile'),
    path('study-planner/', views.study_planner, name='study_planner'),
    path('toggle-task/<int:task_id>/', views.toggle_task, name='toggle_task'),
    path('delete-task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('api/skills/', api_views.skills_api, name='skills_api'),
    path('api/tasks/', api_views.tasks_api, name='tasks_api'),
    path('api/progress/', api_views.progress_api, name='progress_api'),
]