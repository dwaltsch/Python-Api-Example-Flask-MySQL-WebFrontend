## Docker setup instructions
docker build -t flaskserver .
docker run -p 4044:4044 -d flaskserver