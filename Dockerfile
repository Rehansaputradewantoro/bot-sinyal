FROM python:3.11

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

