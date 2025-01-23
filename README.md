## Steps to Run the Project in Docker

cd C:\Users\USER\Desktop
git clone https://github.com/AymanSalman/exam_web_app.git
cd exam_web_app
docker build -t exam_web_app:v1 .
docker run -d -p 80:8017 --name exam-web-app-container exam_web_app:v1
docker ps
