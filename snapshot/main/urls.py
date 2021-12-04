from django.urls import path
from .views import (
    SnapListView, 
    SnapDetailView, 
    SnapCreateView, 
    SnapUpdateView, 
    SnapDeleteView
)
from . import views

#  /snap/5646546546 - strona snapow
#  /search/tag/.... - strona tagow

urlpatterns = [
    #path('', views.home, name='snap-home'),
    path('', SnapListView.as_view(), name='snap-home'),
    path('search/', views.searchTag, name='tag-page'),
    path('snapshot/<int:pk>/', SnapDetailView.as_view(), name='snap-detail'),
    path('snapshot/<int:pk>/update/', SnapUpdateView.as_view(), name='snap-update'),
    path('snapshot/<int:pk>/delete/', SnapDeleteView.as_view(), name='snap-delete'),
    path('snapshot/new/',  SnapCreateView.as_view(), name='snap-create'),
]