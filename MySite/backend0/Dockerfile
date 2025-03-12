FROM python:3.12-slim

WORKDIR /app

COPY MySite/backend0/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY MySite/backend0/src/mysite mysite
EXPOSE 8000

CMD ["uvicorn", "mysite.main:app", "--host", "0.0.0.0", "--port", "8000"]
