## Steps to Run the Project in Docker

### 1. Navigate to the location where you want to clone the project (example directory: Desktop):

```bash
cd C:\Users\USER\Desktop
```bash

### 2. Clone the repository:

```bash
git clone https://github.com/AymanSalman/exam_web_app.git
cd exam_web_app
```bash

### 3. Build the Docker image:

```bash
docker build -t exam_web_app .
```bash

### 4. Run the Docker container:

```bash
docker run -d -p 8017:8017 --name exam_web_app_container exam_web_app
```bash

### 5. Check if the container is running:

```bash
docker ps
```bash

### 6. Access the application:

```bash
[docker run -d -p 8017:8017 --name exam_web_app_container exam_web_app](http://localhost:8017/status/)
```bash
