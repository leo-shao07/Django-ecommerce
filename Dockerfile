# syntax=docker/dockerfile:1

FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt requirements.txt
RUN apt-get update -y \
    # && apt-get install gcc -y \
    # && apt-get install default-libmysqlclient-dev -y \
    && pip3 install -r requirements.txt
COPY . .
EXPOSE 8000
# COPY ./wait-for-it.sh /wait-for-it.sh
RUN chmod +x wait-for-it.sh
# COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x entrypoint.sh
# ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]