from django.conf.urls import url
from django.urls import path
from .views import HomePageView, PostDetailView, AddPostView



app_name = 'feed'

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('detail/<int:pk>/', PostDetailView.as_view(), name = 'detail'),
    path('Post/', AddPostView.as_view(), name='Post')
]