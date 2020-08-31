SOURCE = $(shell find source)

docs: ${SOURCE}
	@echo Building site...
	@python3 ./build-toolchain/build-site.py -s ./settings.cfg