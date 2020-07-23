sudo apt-get update
sudo apt install cmake libtool autoconf libboost-filesystem-dev libboost-iostreams-dev \
libboost-serialization-dev libboost-thread-dev libboost-test-dev  libssl-dev libjsoncpp-dev \
libcurl4-openssl-dev libjsoncpp-dev libjsonrpccpp-dev libsnappy-dev zlib1g-dev libbz2-dev \
liblz4-dev libzstd-dev libjemalloc-dev libsparsehash-dev python3-dev python3-pip
git clone https://github.com/citp/BlockSci.git
cd BlockSci
mkdir release
cd release
CC=gcc-7 CXX=g++-7 cmake -DCMAKE_BUILD_TYPE=Release ..
export CXX=/usr/bin/g++
export CC=/usr/bin/gcc
make
sudo make install
cd ..
CC=gcc-7 CXX=g++-7 sudo -H pip3 install -e blockscipy