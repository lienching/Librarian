FROM python:slim-buster

RUN mkdir librarian

WORKDIR librarian
 
COPY app app
COPY configs.py .
COPY run.py .
COPY requirements.txt .
COPY VERSION .
COPY LICENSE .

RUN pip3 install -r requirements.txt

EXPOSE 39433/tcp

ENTRYPOINT ["python3", "run.py"]
