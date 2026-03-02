from django.urls import include, path
from .views import home_view, registration_view, login_view, logout_view, task_view, complete_task_view, delete_task_view
urlpatterns = [
   path('home/',home_view, name='home'),
   path('add_task/',task_view, name='add_task'),
   path('task/<int:task_id>/complete/', complete_task_view, name='complete_task'),
   path('task/<int:task_id>/delete/', delete_task_view, name='delete_task'),
   path('register/',registration_view, name='register'),
   path('login/',login_view, name='login'),
   path('logout/',logout_view, name='logout'),
]
