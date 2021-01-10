FROM python:3.8-buster

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt


EXPOSE 80

CMD ["uvicorn", "run:app", "--host", "0.0.0.0", "--port", "80"]