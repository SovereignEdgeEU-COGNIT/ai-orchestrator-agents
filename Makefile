all: build

.PHONY: build 
build:
	python3 setup.py sdist bdist_wheel

.PHONY: test
test:
	@python3 ./test/envclient_test.py

.PHONY: install
install:
	pip3 install dist/envclient-1.0.0-py3-none-any.whl --force-reinstall 

publish:
	python3 -m twine upload dist/envclient-1.0.0-py3-none-any.whl 
