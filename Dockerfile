FROM python:3.9.6

WORKDIR /usr/src/app

COPY ./sttCheckin/ ./
RUN pip install --no-cache-dir -r ./requirements.txt


CMD [ "/bin/bash", "./entrypoint.sh" ]