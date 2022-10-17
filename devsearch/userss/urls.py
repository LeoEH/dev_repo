from django.urls import path
from . import views

urlpatterns = [
	path('profiles', views.profiles, name='profiles'),
	path('profile/<str:pk>/', views.userProfile, name="user-profile"),
	path('test', views.test, name='test')
]