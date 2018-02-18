dependencies:
	pip install flask
	pip install markdown
	pip install Frozen-Flask

clean:
	lsof -ti:5000 | xargs kill

static:
	mypy --ignore-missing-imports `find . -name *.py`

build:
	python main.py