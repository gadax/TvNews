FROM python:3.9

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]