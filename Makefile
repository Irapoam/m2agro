clean:
	find . -name "*.pyc" -exec rm -rf {} \;
run: clean
	python3 manage.py runserver 0.0.0.0:8000 --settings=m2agro.settings_local
migrate:
	python3 manage.py migrate --settings=m2agro.settings_local
migrations:
	python3 manage.py makemigrations --settings=m2agro.settings_local
install:
	pip3 install -r requirements.txt
	make migrate
user:
	python3 manage.py createsuperuser --settings=m2agro.settings_local

shell:
	python3 manage.py shell --settings=m2agro.settings_local

tests: clean
	python3 manage.py test --settings=m2agro.settings_tests

run_celery:
	celery worker -l info --beat --app=m2agro.celery:app
	
initial_deploy:
	cap $(stage) setup:install_requirements_server
	cap $(stage) deploy
	cap $(stage) setup:create_folders
	cap $(stage) setup:install_requirements
	cap $(stage) setup:conf_files
	cap $(stage) setup:migrations
	cap $(stage) setup:collect_static
	cap $(stage) setup:restart_app

deploy:
	cap $(stage) deploy
	cap $(stage) setup:install_requirements
	cap $(stage) setup:migrations
	cap $(stage) setup:collect_static
	cap $(stage) setup:restart_app