.PHONY: build

build:
	rm -rf build/
	cookiecutter . -o build/
