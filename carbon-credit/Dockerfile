FROM python:3.10

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt
COPY . /app

ENTRYPOINT [ "python" ]
EXPOSE 8010

CMD ["app.py","8010"]