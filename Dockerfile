FROM python:3.10
WORKDIR /app
COPY . /app
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
EXPOSE 8080
CMD ["gunicorn","--config", "gunicorn_config.py", "main:app"]




#build according to https://www.youtube.com/watch?v=7CvD6oHmYxU
# Build image for GCP (only need this becuase of M1 chip)
#docker buildx build -t menu-time-flask --platform linux/amd64 .

# Tag Image for GCP
#docker tag menu-time-flask gcr.io/plan-your-grub/menu-time-flask

#gcloud auth login
#gcloud auth configure-docker
#docker push gcr.io/plan-your-grub/menu-time-flask