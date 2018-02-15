dependencies:
	pip install flask
	pip install markdown

clean:
	lsof -ti:5000 | xargs kill

build:
	python main.py