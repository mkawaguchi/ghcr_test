FROM bitnami/minideb:latest

# Install Base Packages
RUN \
 install_packages \
    ansible \
	bash \
	curl \
    git \
	less \ 
	mongo-tools \
	net-tools \
	ssh \
	tzdata \
	unzip \
	vim-tiny \
    wget

# Install Mongo
RUN \
 mkdir -p /data/db/tmp && cd /data/db/tmp/ \
 wget -q https://repo.mongodb.org/apt/debian/dists/buster/mongodb-org/4.4/main/binary-amd64/mongodb-org-shell_4.4.4_amd64.deb; \
 wget -q https://repo.mongodb.org/apt/debian/dists/buster/mongodb-org/4.4/main/binary-amd64/mongodb-org-server_4.4.4_amd64.deb; \
 apt install /data/db/tmp/mongodb-org-shell_4.4.4_amd64.deb; \
 apt install /data/db/tmp/mongodb-org-server_4.4.4_amd64.deb; \
 rm /data/db/tmp/*.deb