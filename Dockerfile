FROM python:3.10
WORKDIR /
COPY . /
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
EXPOSE 8080
#CMD python ./main.py
CMD ["gunicorn","--config", "gunicorn_config.py", "main:app"]


#docker build -t mrende1986/menutime:0.0.1.RELEASE .
#docker run -p 3000:3005 -d mrende/menutime:0.0.1.RELEASE
#gunicorn --config gunicorn_config.py main:app

#build according to https://www.youtube.com/watch?v=7CvD6oHmYxU

# Build image for GCP (only need this becuase of M1 chip)
#docker buildx build -t menutime --platform linux/amd64 .

# Tag Image for GCP
#docker tag menutime gcr.io/plan-your-grub/menutime

#gcloud auth login
#gcloud auth configure-docker
#docker push gcr.io/plan-your-grub/menutime