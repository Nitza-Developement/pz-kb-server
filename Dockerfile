FROM python:3.12.6-alpine3.20

ENV PYTHONUNBUFFERED=1

WORKDIR /app


RUN apk update && \
    apk add --no-cache gcc musl-dev python3-dev libffi-dev && \
    pip install --upgrade pip

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
