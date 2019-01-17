FROM continuumio/anaconda3:latest
COPY . /app
COPY ./gcloud /root/.config/gcloud
RUN conda install python=3.6.5 -y
RUN pip install -r ./app/requirements.txt
RUN pip install tensorflow
RUN apt update
RUN apt install build-essential -y
#RUN conda upgrade --all -y
#RUN conda install -c anaconda swig
#RUN pip install mecab-python3
RUN apt install git make sudo -y
#RUN cd tmp; git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git;
#RUN cd /tmp/mecab-ipadic-neologd; ./bin/install-mecab-ipadic-neologd -n -y
#RUN cd /app; cat mecabrc > /etc/mecabrc
WORKDIR /app
CMD python3 00-wrapper.py
