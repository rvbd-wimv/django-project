FROM python:3.9-slim-buster

RUN apt-get update && apt-get install -y --no-install-recommends python3 python3-pip

COPY requirements.txt /opt/app/
COPY startup-dj.sh /opt/app/
RUN chmod +x /opt/app/startup-dj.sh

WORKDIR /opt/app
RUN pip install -r requirements.txt
RUN django-admin startproject nightlife
RUN cd /opt/app/nightlife
RUN django-admin startapp m_api

COPY ./m_api/*.py /opt/app/nightlife/m_api/
COPY ./nightlife/*.py /opt/app/nightlife/nightlife/

EXPOSE 8000

ENTRYPOINT ["bash","/opt/app/startup-dj.sh"]
