FROM python:3.9-slim
WORKDIR /Assignment-03
COPY Assignment-03.py /Assignment-03
CMD [ "python","Assignment-03.py" ]