FROM python:3.8-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD gunicorn --workers=4 0.0.0.0:$PORT app:app