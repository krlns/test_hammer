FROM python:3.9

COPY requirements.txt /temp/requirements.txt
COPY auth /auth

WORKDIR /auth

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install -r /temp/requirements.txt
RUN python manage.py makemigrations --noinput
RUN python manage.py migrate --noinput

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]