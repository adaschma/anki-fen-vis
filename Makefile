.PHONY: error install uninstall

INSTALL_DIR = "/Users/andrewl/Library/Application\ Support/Anki2/addons21"

error:
	@echo "available targets: install, uninstall"
	@exit -1

install:
	@if [ -L "$(INSTALL_DIR)/841766736" ]; then \
		echo "already installed"; \
	else \
		echo "installing"; \
		ln -s "$(PWD)/distribution" "$(INSTALL_DIR)/841766736"; \
	fi

uninstall:
	@if [ -L "$(INSTALL_DIR)/841766736" ]; then \
		echo "uninstalling"; \
		rm "$(INSTALL_DIR)/841766736"; \
	else \
		echo "not installed"; \
	fi

share:
	rm -rf ./distribution/__pycache__ ./distribution/*.pyc
	rm -rf ./distribution/chess/__pycache__ ./distribution/chess/*.pyc
	pushd ./distribution && zip -r ../anki-fen-viz.zip * && popd
