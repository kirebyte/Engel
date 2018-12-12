.DEFAULT_GOAL := build

#Colorized echo
define echo-status
      @tput setaf 3
      @echo $1
      @tput sgr0
endef

build: clean compile-virtualenv

clean: clean-cache clean-virtualenv

clean-cache:
	$(call echo-status,"Cleaning python cache...")
	@rm -rf commands/__pycache__
	@rm -rf responses/__pycache__
	@rm -rf plugins/__pycache__
	@rm -rf utilities/__pycache__

clean-virtualenv:
	$(call echo-status,"Cleaning virtualenv...")
	@rm -rf lib

compile-virtualenv:
	$(call echo-status,"Downloading and installing virtualenv dependencies...")
	@virtualenv -p python3 lib
	@lib/bin/pip install -r build/dependencies

debug:	build
	$(call echo-status,"Setting engel file as runnable...")
	@chmod +x engel.py

install: install-engel install-config install-service

install-config:
	$(call echo-status,"Installing configuration snippet...")
	@mkdir -p /etc/opt/engel
	@cp build/config /etc/opt/engel
	$(call echo-status,"Please configure your API key in /etc/opt/engel/config")

install-engel:
	$(call echo-status,"Installing /opt/engel...")
	@mkdir -p /opt/engel
	@cp -r commands /opt/engel
	@cp -r integrations /opt/engel
	@cp -r lib /opt/engel
	@cp -r plugins /opt/engel
	@cp -r responses /opt/engel
	@cp -r utilities /opt/engel
	@cp __init__.py /opt/engel
	@cp engel.py /opt/engel/engel
	@chmod +x /opt/engel

install-service:
	$(call echo-status,"Installing service...")
	@cp build/service/engel.service /lib/systemd/system
	@systemctl enable engel
	@service engel start

uninstall: uninstall-service uninstall-engel uninstall-config

uninstall-config:
	$(call echo-status,"Removing configuration file...")
	@sudo rm -rf /etc/opt/engel

uninstall-engel:
	$(call echo-status,"Removing Engel...")
	@rm -rf /opt/engel

uninstall-service:
	$(call echo-status,"Removing Engel service...")
	@service engel stop
	@systemctl disable engel
	@rm /lib/systemd/system/engel.service
