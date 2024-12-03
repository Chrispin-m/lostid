from django.urls import path
from . import views

urlpatterns = [
    path('', views.FoundIDListView.as_view(), name='found_id_list'),
    path('<uuid:id>/', views.FoundIDDetailView.as_view(), name='found_id_detail'),
    path('post/', views.PostFoundID.as_view(), name='post_found_id'),
    path('search/', views.SearchLostID.as_view(), name='search_lost_id'),
    path('<uuid:id>/messages/', views.FoundIDMessagesView.as_view(), name='found_id_messages'),
    path('<uuid:id>/messages/post/', views.PostMessage.as_view(), name='post_message'),
]
