FROM python:3.8

ADD main.py .

EXPOSE 8050/tcp

RUN pip install psycopg2 dash pandas

CMD [ "python", "./main.py" ]

