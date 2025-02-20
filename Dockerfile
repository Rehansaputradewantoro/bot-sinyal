# Gunakan image Python 3.11 sebagai dasar
FROM python:3.11

# Atur direktori kerja
WORKDIR /app

# Salin semua file ke dalam container
COPY . .

# Instal dependensi yang diperlukan
RUN pip install --no-cache-dir -r requirements.txt

# Jalankan bot secara otomatis
CMD ["python", "main.py"]

