FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install google-adk

EXPOSE 8000

CMD ["adk", "web"]
