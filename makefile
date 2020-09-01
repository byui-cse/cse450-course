docs: FORCE clean
	@echo Building site...
	@python3 ./build-toolchain/build-site.py -s ./settings.cfg

FORCE:

clean:
	@echo Cleaning site...
	@rm -rf ./docs

local: clean
	@echo Building local site
	@python3 ./build-toolchain/build-site.py -s ./settings-local.cfg
