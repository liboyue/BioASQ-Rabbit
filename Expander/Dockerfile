FROM docker.lappsgrid.org/deiis/base

RUN pip install pymetamap
COPY . /root/
WORKDIR /root
ENTRYPOINT ["python", "service.py"]
