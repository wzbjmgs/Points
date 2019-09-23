FROM python:3.7

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip --no-cache-dir install -r requirements.txt
RUN python setup.py install

CMD bash run.sh "5 5" "[['1 2 N', 'LMLMLMLMM'], ['3 3 E', 'MMRMMRMRRM']]"