FROM python:3.8

COPY http-server.py .

CMD ["python3", "http-server.py"]
