FROM python:3.11-slim

WORKDIR /app/

COPY requirements.txt /app/

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver"]