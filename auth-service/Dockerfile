FROM python

COPY main.py /app/main.py
COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

CMD ["python", "/app/main.py"]