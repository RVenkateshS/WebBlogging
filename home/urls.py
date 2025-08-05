 
  
from django.urls import path
from .views import HomeView
from .views import ArticalDetailView , AddPostView,UpdatePostView ,DeletePostView

urlpatterns = [
  path('', HomeView.as_view(), name='home'),
  path('article/<int:pk>', ArticalDetailView.as_view(), name = 'article-detail'),
  path('AddPost/',AddPostView.as_view(), name= 'AddPost' ),
  path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
  path('article/remove/<int:pk>', DeletePostView.as_view(), name='delete_post'),
  
]
  
  


