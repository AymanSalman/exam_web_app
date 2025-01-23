FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
EXPOSE 8017
RUN python manage.py migrate
CMD ["python", "manage.py", "runserver", "0.0.0.0:8017"]
