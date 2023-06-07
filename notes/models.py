from django.db import models


class Penulis(models.Model):
    nama = models.CharField(max_length=100)
    usia = models.IntegerField()

    def __str__(self):
        return self.nama


class Catatan(models.Model):
    judul = models.CharField(max_length=100)
    penerbit = models.CharField(max_length=100)
    pembuat = models.ForeignKey(
        Penulis, related_name='catatan', on_delete=models.CASCADE)

    def __str__(self):
        return self.judul
