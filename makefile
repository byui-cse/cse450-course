docs: FORCE
	@echo Building site...
	@python3 ./build-toolchain/build-site.py -s ./settings.cfg

FORCE:

clean:
	rm -rf ./docs