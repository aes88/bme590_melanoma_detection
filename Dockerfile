from gcr.io/tensorflow/tensorflow:latest
RUN pip install Flask
RUN pip install -U flask-cors
RUN pip install pymodm
ENV FLASK_APP=main.py
