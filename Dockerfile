FROM python:3

WORKDIR /api

RUN pip3 install --upgrade pip
RUN pip3 install requests

COPY . .

CMD [ "python", "api.py" ]