.PHONY: error install uninstall

INSTALL_DIR = "/Users/andrewl/Library/Application\ Support/Anki2/addons21/841766736"

error:
	@echo "available targets: install, uninstall"
	@exit -1

install:
	@if [ -L "$(INSTALL_DIR)" ]; then \
		echo "already installed (symlink to dev directory)"; \
	elif [ -d "$(INSTALL_DIR)" ]; then \
		echo "already installed (directory from add-on manager)"; \
	else \
		echo "installing"; \
		ln -s "$(PWD)/distribution" "$(INSTALL_DIR)"; \
	fi

uninstall:
	@if [ -L "$(INSTALL_DIR)" ]; then \
		echo "uninstalling"; \
		rm "$(INSTALL_DIR)"; \
	elif [ -d "$(INSTALL_DIR)" ]; then \
		echo "actual directory found, uninstall with add-on manager"; \
	else \
		echo "not installed"; \
	fi

share:
	rm -rf ./distribution/__pycache__ ./distribution/*.pyc
	rm -rf ./distribution/chess/__pycache__ ./distribution/chess/*.pyc
	pushd ./distribution && zip -r ../anki-fen-viz.zip * && popd
