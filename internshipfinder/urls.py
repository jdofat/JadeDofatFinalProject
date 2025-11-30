# to django: what page loads when someone visits a link
# map: URL matched to view
# django runs code when link is clicked

from django.contrib import admin
from django.urls import path
from internships import views

urlpatterns = [
    path('admin/', admin.site.urls),  # admin page
    path('', views.home, name='home'),
    path('results/', views.results, name='results'),
    path('internship/<str:internship_id>/', views.internship_detail, name='internship_detail'),
    path('login/', views.admin_login, name='login'),
    path('create/', views.create_admin, name='create'),
    path('delete/<str:internship_id>/', views.delete_internship, name='delete'),  # changed from <int:internship_id> to <str:internship_id>
]
