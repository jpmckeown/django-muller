from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='splash'),
    path('blog/', views.allposts, name='blogindex'),
    path('blog/<slug:slug>', views.onepost, name='onepost')
]
