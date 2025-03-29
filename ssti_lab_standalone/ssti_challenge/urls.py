from django.urls import path
from . import views

urlpatterns = [
    path("", views.ssti, name="SSTI"),
    path("lab/", views.ssti_challenge, name="SSTI Lab"),
    path("blog/<str:blog_id>/", views.ssti_view_blog, name="SSTI View Blog"),
    path("challenge/", views.ssti_challenge, name="SSTI Challenge"),
]