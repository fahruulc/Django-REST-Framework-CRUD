from rest_framework import generics
from .models import Penulis, Catatan
from .serializers import PenulisSerializer, CatatanSerializer


class PenulisListCreateAPIView(generics.ListCreateAPIView):
    queryset = Penulis.objects.all()
    serializer_class = PenulisSerializer


class PenulisRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Penulis.objects.all()
    serializer_class = PenulisSerializer


class CatatanListCreateAPIView(generics.ListCreateAPIView):
    queryset = Catatan.objects.all()
    serializer_class = CatatanSerializer


class CatatanRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Catatan.objects.all()
    serializer_class = CatatanSerializer
