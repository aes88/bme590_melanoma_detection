from gcr.io/tensorflow/tensorflow:latest
RUN pip install Flask
RUN pip install -U flask-cors
ENV FLASK_APP=main.py
