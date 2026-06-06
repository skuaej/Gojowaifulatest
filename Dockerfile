FROM python:3.11-slim

ENV PIP_NO_CACHE_DIR=1

RUN apt-get update && apt-get install -y git

RUN pip install --upgrade pip setuptools

COPY . /app/

WORKDIR /app/

RUN pip install --no-cache-dir -U -r requirements.txt

CMD ["python3", "-m", "TEAMZYRO"]
