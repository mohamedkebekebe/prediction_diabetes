FROM python:3.8=slim

WORKDIR  /app_html

COPY ./app_html

RUN  pip install -r requirements.txt

EXPOSE  80

CMD   uvicorn app_html:app ==host 0.0.0.0 ==port ${PORT 