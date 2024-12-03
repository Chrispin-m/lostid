from django.urls import path
from .views import PostFoundID, SearchLostID, PostMessage

urlpatterns = [
    path('post/', PostFoundID.as_view(), name='post-found-id'),
    path('search/', SearchLostID.as_view(), name='search-lost-id'),
    path('message/<uuid:id>/', PostMessage.as_view(), name='post-message'),
]
