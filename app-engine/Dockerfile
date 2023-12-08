FROM python

WORKDIR /app

ADD ["app.py", "requirements.txt", "./"]

RUN ["pip", "install", "-r", "./requirements.txt"]

ENV PORT "8080"

EXPOSE 8080

CMD ["sh", "-c", "flask run --port=$PORT --host=0.0.0.0"]
