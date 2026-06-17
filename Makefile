install:
	pip install -r requirements.txt

test:
	PYTHONPATH=src pytest -q

freeze:
	pip freeze > requirements-lock.txt

tree:
	find . -maxdepth 3 -type f | sort

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
