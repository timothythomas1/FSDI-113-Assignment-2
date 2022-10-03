from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostDeleteView,
    PostUpdateView,
    DraftPostListView,
    ArchivedPostListView,
    PublishedPostListView
)

# The 'name' is the name of the HTML name in Templates
urlpatterns = [
    path('', PostListView.as_view(), name='list'),
    path('drafts/', DraftPostListView.as_view(), name='draft_list'),
    path('archived/', ArchivedPostListView.as_view(), name='archived_list'),
    path('published/', PublishedPostListView.as_view(), name='published_list'),
    path('<int:pk>', PostDetailView.as_view(), name='detail'),
    path('new/', PostCreateView.as_view(), name='new'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='confirm_delete'),
]