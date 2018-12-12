#!/bin/bash
export TERM='xterm-256color'
export PATH='/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'

{
	echo "Upgrade started at $(date)"
	rm -rf /tmp/engel
	cd /tmp/ && \
	wget -N 'https://www.dropbox.com/s/imb2ulyme69dkjh/engel.tar.gz' && \
	tar -xf engel.tar.gz && \
	cd /tmp/engel && \
	make && \
	service engel stop && \
	cd /tmp/engel && \
	make uninstall-engel && \
	cd /tmp/engel && \
	make install-engel && \
	service engel start && \
	rm /tmp/engel.tar.gz && \
	rm -rf /tmp/engel
	echo "Upgrade finished at $(date)"
} &> /var/log/engel.log
