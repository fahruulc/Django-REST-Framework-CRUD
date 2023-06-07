# Django-REST-Framework-CRUD

CRUD implementation with DRF using Generics Views

1. Endpoint untuk Penulis:
   GET /api/penulis/: Mendapatkan daftar semua penulis.
   GET /api/penulis/{id}/: Mendapatkan detail penulis berdasarkan ID.
   POST /api/penulis/: Membuat penulis baru.
   PUT /api/penulis/{id}/: Memperbarui penulis yang ada berdasarkan ID.
   DELETE /api/penulis/{id}/: Menghapus penulis yang ada berdasarkan ID.
2. Endpoint untuk Catatan:
   GET /api/catatan/: Mendapatkan daftar semua catatan.
   GET /api/catatan/{id}/: Mendapatkan detail catatan berdasarkan ID.
   POST /api/catatan/: Membuat catatan baru.
   PUT /api/catatan/{id}/: Memperbarui catatan yang ada berdasarkan ID.
   DELETE /api/catatan/{id}/: Menghapus catatan yang ada berdasarkan ID.

# Run Program

0. pip install -r requirements.txt
1. py manage.py makemigrations
2. py manage.py migrate
3. py manage.py runserver

# Response

Response get all notes :
{
"id": 1,
"judul": "Raden Kian Santang",
"penerbit": "Gajah Mada",
"pembuat": 1
},
