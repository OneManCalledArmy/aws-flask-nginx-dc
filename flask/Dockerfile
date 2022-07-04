FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
CMD gunicorn --workers=3 --bind 0.0.0.0:5000 wsgi:app
#CMD python3 app.py
