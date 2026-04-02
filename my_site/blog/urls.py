from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.allposts, name='blogindex'),
    path('blog/<slug:slug>', views.post, name='onepost')
]
