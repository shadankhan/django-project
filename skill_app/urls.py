from django.urls import path
from skill_app import views

urlpatterns = [
    
    path('all_projects', views.project, name="project"),
    path('profile', views.profile, name="profile"),
    path('c_profile', views.create_profile, name="create_profile"),
]
