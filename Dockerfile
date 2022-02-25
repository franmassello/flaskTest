FROM alpine:latest

RUN apk add --no-cache python3 \
    && apk add --update py-pip \
    && pip3 install --upgrade pip \
    && pip3 install --upgrade setuptools 

WORKDIR /app
COPY . /app
RUN pip3 --no-cache-dir install -r requirements.txt
EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["main.py"]