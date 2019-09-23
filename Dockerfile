FROM python:3.7

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip --no-cache-dir install -r requirements.txt
RUN python setup.py install

ENTRYPOINT python -m ./points/app.py