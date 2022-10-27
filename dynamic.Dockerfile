FROM: ubuntu:jammy
COPY: ./volumes/jcb_dynamic /JCBDemo/
RUN dpkg --configure -a
RUN apt-get update
RUN apt-get install -y git python3 python3-pip python-is-python3 python3.10-venv
RUN cd /JCBDemo/
RUN python -m pip install -r requirements.txt
RUN python main.py

