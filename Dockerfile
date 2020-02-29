from registry-vpc.cn-hangzhou.aliyuncs.com/eigenlab/eigen-jnlp-slave-py35

run mkdir -p /pony
COPY . /pony/
RUN pip3 install -r /pony/requirements.txt


#install dumb-init
RUN apt-get update && apt-get install -y wget && \
wget https://github.com/Yelp/dumb-init/releases/download/v1.2.1/dumb-init_1.2.1_amd64.deb && \
dpkg -i dumb-init_*.deb && rm dumb-init_*.deb
# install yud executor


RUN wget https://eigencdn.oss-cn-hangzhou.aliyuncs.com/yud/release/executor-amd64 -O /usr/bin/executor \
    && chmod +x /usr/bin/executor

WORKDIR /pony

