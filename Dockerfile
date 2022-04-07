FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD uvicorn main:app --reload
CMD python3 models.py


