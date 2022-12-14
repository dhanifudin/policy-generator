FROM python:3.8-alpine
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY ./app /app
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
EXPOSE 8000
