FROM python:3.8-alpine

WORKDIR /

RUN pip3 install pip==19.0.3 --no-cache-dir

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt --no-cache-dir

COPY ./* .

CMD ['cd', 'app']
CMD [ "uvicorn", "index:app", "--reload", "--host", "0.0.0.0"]