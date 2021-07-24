FROM python:3.8
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements /code/
COPY .env /code/
RUN pip install -r dev.txt
COPY . /code/
