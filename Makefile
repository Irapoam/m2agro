clean:
	find . -name "*.pyc" -exec rm -rf {} \;
run: clean
	python3 manage.py runserver 0.0.0.0:8000 --settings=m2agro.settings_local
migrate:
	python3 manage.py migrate --settings=m2agro.settings_local
migrations:
	python3 manage.py makemigrations --settings=m2agro.settings_local
install:
	npm install
	# bower install
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
	cap production setup:install_requirements_server
	cap production deploy
	cap production setup:create_folders
	cap production setup:install_requirements
	cap production setup:conf_files
	cap production setup:migrations
	cap production setup:collect_static
	cap production setup:restart_app
	

deploy:
	cap production deploy
	cap production setup:install_requirements
	cap production setup:migrations
	cap production setup:collect_static
	cap production setup:restart_app