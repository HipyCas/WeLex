FROM python:3.8-alpine

RUN adduser -D welex

WORKDIR /home/welex

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY migrations migrations
COPY welex.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP welex.py

RUN chown -R welex:welex ./
USER welex

EXPOSE 5000
ENTRYPOINT [ "./boot.sh" ]