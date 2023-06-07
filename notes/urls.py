from django.urls import path
from .views import PenulisListCreateAPIView, PenulisRetrieveUpdateDestroyAPIView, CatatanListCreateAPIView, CatatanRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('penulis/', PenulisListCreateAPIView.as_view(),
         name='penulis-list-create'),
    path('penulis/<int:pk>/', PenulisRetrieveUpdateDestroyAPIView.as_view(),
         name='penulis-retrieve-update-destroy'),
    path('catatan/', CatatanListCreateAPIView.as_view(),
         name='catatan-list-create'),
    path('catatan/<int:pk>/', CatatanRetrieveUpdateDestroyAPIView.as_view(),
         name='catatan-retrieve-update-destroy'),
]
