FROM python:3.8

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

# for dev
ENV PYTHONDONTWRITEBYTECODE 1

# Install dependencies
RUN apt-get update && apt-get install -y vim libffi-dev libnacl-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install -U pip pipenv

# Create the application directory
RUN set -ex && mkdir -p /app
WORKDIR /app

# Adding Pipfiles
COPY Pipfile /app/Pipfile
COPY Pipfile.lock /app/Pipfile.lock

# Install dependencies
RUN pipenv install --deploy --system --dev

CMD ["/bin/bash"]

