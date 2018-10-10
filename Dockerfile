FROM python:3.6

RUN mkdir -p /app
ADD . /app

WORKDIR /app

EXPOSE 8000

RUN pip install .

CMD gunicorn myapp.main:app --bind 0.0.0.0:8000 --worker-class aiohttp.worker.GunicornWebWorker
