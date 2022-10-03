from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostDeleteView,
    PostUpdateView
)


# The 'name' is the name of the HTML name in Templates
urlpatterns = [
    path('', PostListView.as_view(), name='list'),
    path('<int:pk>', PostDetailView.as_view(), name='detail'),
    path('new/', PostCreateView.as_view(), name='new'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='confirm_delete'),
]