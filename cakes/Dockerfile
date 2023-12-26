FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# working directory in the container
WORKDIR /cakes_container

COPY requirements.txt /cakes_container/

RUN pip install -r requirements.txt

COPY cakes /cakes_container/

# Open the port the app runs on
EXPOSE 8000

CMD ["gunicorn", "cakes_container.wsgi:application", "--bind", "0.0.0.0:8000"]
