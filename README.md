## Steps to Run the Project in Docker

cd C:\Users\USER\Desktop

git clone https://github.com/AymanSalman/exam_web_app.git
cd exam_web_app

docker build -t exam_web_app .

docker run -d -p 8017:8017 --name exam_web_app_container exam_web_app

docker ps
