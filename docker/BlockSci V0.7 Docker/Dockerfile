FROM ubuntu:bionic

USER root
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    rm -rf /var/lib/apt/lists/*
	
RUN add-apt-repository ppa:ubuntu-toolchain-r/test -y
RUN apt-get update

RUN apt install -y cmake libtool autoconf libboost-filesystem-dev libboost-iostreams-dev \
	libboost-serialization-dev libboost-thread-dev libboost-test-dev  libssl-dev libjsoncpp-dev \
	libcurl4-openssl-dev libjsoncpp-dev libjsonrpccpp-dev libsnappy-dev zlib1g-dev libbz2-dev \
	liblz4-dev libzstd-dev libjemalloc-dev libsparsehash-dev python3-dev python3-pip git

RUN cd /root && git clone https://github.com/citp/BlockSci.git && \
	cd BlockSci && \
	mkdir release && \
	cd release && \
	CC=gcc-7 CXX=g++-7 cmake -DCMAKE_BUILD_TYPE=Release .. && \
	make && \
	make install && \
	cd .. && \
	CC=gcc-7 CXX=g++-7 && \
	pip3 install -e blockscipy && \
    pip3 install multiprocess psutil jupyter pycrypto matplotlib pandas dateparser requests findspark tqdm networkx

RUN cd /root && \
    curl -L https://github.com/krallin/tini/releases/download/v0.6.0/tini > tini && \
    echo "d5ed732199c36a1189320e6c4859f0169e950692f451c03e7854243b95f4234b *tini" | sha256sum -c - && \
    mv tini /usr/local/bin/tini && \
    chmod +x /usr/local/bin/tini

RUN mkdir -p -m 700 /root/.jupyter/ && \
    echo "c.NotebookApp.ip = '*'" >> /root/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.password = u'sha1:b7059f178a65:0f131166db948c9d7df378dc378ecd661b490d3e'" >> /root/.jupyter/jupyter_notebook_config.py

WORKDIR /root/BlockSci/Notebooks

ENTRYPOINT ["tini", "--"]
CMD jupyter notebook --ip 0.0.0.0 --no-browser --port=8888 --allow-root
