FROM python:3.8

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install --upgrade pip

# dependency for debug and remote attach.
RUN pip install debugpy==1.2.1 ipython==8.2.0

RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY . /app