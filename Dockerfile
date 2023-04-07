# For more information, please refer to https://aka.ms/vscode-docker-python
FROM ubuntu:22.04

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN apt-get update && \
    apt-get install -yqq --no-install-recommends build-essential gcc python3-dev python3 python3-pip mysql-client libmysqlclient-dev && \
    pip3 install -r requirements.txt && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /duck-it
COPY . /duck-it

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /duck-it
USER appuser

# CMD ["python3", "manage.py", "makemigrations"]
# CMD ["python3", "manage.py", "migrate"]
CMD ["python3", "manage.py", "runserver", "0.0.0.0:3000"]
