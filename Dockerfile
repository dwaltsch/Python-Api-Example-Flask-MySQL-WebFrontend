FROM python:3.8-alpine
WORKDIR /flask
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
Copy ./Flask/secrets.txt ./
Copy ./Flask/main.py ./
CMD [ "python3", "main.py"]