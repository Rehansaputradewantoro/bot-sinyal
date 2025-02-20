# Gunakan image Python 3.11 sebagai dasar
FROM python:3.11

# Atur direktori kerja
WORKDIR /app

# Salin semua file ke dalam container
COPY . .

# Instal dependensi yang diperlukan
RUN pip install --no-cache-dir -r requirements.txt

# Jalankan script untuk memuat variabel dari sample.env
CMD ["python", "load_env.py"]

Set working directory

WORKDIR /app

Copy all necessary files

COPY . /app

Install dependencies

RUN pip install --upgrade pip 
&& pip install -r requirements.txt

Set environment variables

ENV PYTHONUNBUFFERED=1

Run the bot

CMD ["python", "main.py"]

