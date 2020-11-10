FROM python:3.7.3-slim
ARG SECRET_KEY
ARG ENVIRONMENT=dev
ENV ENVIRONMENT=$ENVIRONMENT
ENV SECRET_KEY=$SECRET_KEY
RUN apt-get update
WORKDIR /opt
COPY requirements.txt ./
RUN pip install rcssmin --install-option="--without-c-extensions"
RUN pip install --no-cache-dir -r requirements.txt && rm requirements.txt
COPY . ./

RUN python manage.py collectstatic --noinput --clear

EXPOSE 5000

ENTRYPOINT [ "/bin/bash", "-c", "gunicorn -w 2 -b 0.0.0.0:5000 together.wsgi:application --log-level debug" ]
