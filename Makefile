build:
	rm -rf dist/
	python -m build 
	twine upload dist/*  --verbose
