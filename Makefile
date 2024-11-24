install:
	pip install -r requirements.txt

test:
	pytest tests/

run:
	python main.py $(operation) $(a) $(b)
