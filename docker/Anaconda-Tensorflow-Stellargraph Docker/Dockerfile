FROM ubuntu:bionic

USER root
WORKDIR /home/ubuntu/

RUN apt-get update
RUN apt install -y  curl wget

RUN wget https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh
RUN bash Anaconda3-2020.07-Linux-x86_64.sh -b
RUN echo "export PATH="/root/anaconda3/bin:$PATH"" >> ~/.bashrc
RUN /bin/bash -c "source ~/.bashrc"
RUN /bin/bash -c "source /root/anaconda3/bin/activate"
ENV PATH /root/anaconda3/bin:$PATH
RUN rm /home/ubuntu/Anaconda3-2020.07-Linux-x86_64.sh

RUN pip install tensorflow
RUN pip install stellargraph

RUN jupyter notebook --generate-config --allow-root && \
    echo "c.NotebookApp.password = u'sha1:6a3f528eec40:6e896b6e4828f525a6e20e5411cd1c8075d68619'" >> /home/ubuntu/.$
		
CMD jupyter notebook --ip 0.0.0.0 --no-browser --port=8888 --allow-root