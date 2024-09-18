run_server:
	FLASK_APP=app:server flask run --reload

run_tests:
	python -m unittest discover -s tests

run_coverage:
	python -m coverage run ./tests/users/users_mapper_test.py ./tests/users/users_service_test.py
	python -m coverage report
	python -m coverage html

run_coverages:
	python -m coverage run ./tests/users/users_mapper_test.py
	python -m coverage run ./tests/users/users_service_test.py
	python -m coverage combine
	python -m coverage report -m