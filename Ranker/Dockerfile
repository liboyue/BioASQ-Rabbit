FROM docker.lappsgrid.org/bioasq-rabbit/base

RUN pip install pymetamap nltk sklearn werkzeug lxml diskcache pyquery pika
COPY . /root/
WORKDIR /root
ENTRYPOINT ["python", "service.py"]
