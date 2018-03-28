FROM docker.lappsgrid.org/deiis/base

COPY . /
ENTRYPOINT ["bash", "/start.sh"]
#ENTRYPOINT ["python", "/Splitter/service.py"]
