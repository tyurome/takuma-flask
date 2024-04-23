FROM python:3.11.5-slim-bullseye

WORKDIR /app

COPY ./app/requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./app /app

CMD ["python", "main.py"]