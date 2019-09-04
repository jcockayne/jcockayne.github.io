docker build -t personal_website .
docker run -v "$(pwd)"/app:/app -p 80:80 -i -t personal_website