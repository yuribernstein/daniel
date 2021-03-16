FROM python:3
COPY ./templates/* /DC/templates/
COPY ./* /DC/
WORKDIR /DC
RUN pip3 install --no-cache-dir -r requirements.txt
ENV LOG_FILE_LOCATION=/tmp/log.json
EXPOSE 80
ENV FLASK_APP=web_server.py
ENTRYPOINT [ "bash", "init.sh" ]