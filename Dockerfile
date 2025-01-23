#1. Base Image
FROM python:3.9-slim

#2. Working Directory
WORKDIR /app

#3. Copy files
COPY . /app/

#4. Install Dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

#5. Expose Port
EXPOSE 8000

#6. Environment Variable
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

#7. Command to start app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]