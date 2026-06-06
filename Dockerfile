FROM python:3.8.5-slim-buster

ENV PIP_NO_CACHE_DIR=1

RUN apt-get update && apt-get install -y git

RUN pip3 install --upgrade pip setuptools

COPY . /app/
WORKDIR /app/

RUN pip3 install --no-cache-dir -U -r requirements.txt

CMD ["python3", "-m", "TEAMZYRO"]
