build:
	# Build and run migrations and setup dummy data and create a default admin account
	docker-compose build
	docker-compose run web python manage.py makemigrations
	docker-compose run web python manage.py migrate
	docker-compose run web python manage.py setup_dummy_data
	docker-compose run web python manage.py create_admin

run:
	# Start the docker container
	docker-compose up -d


kill:
	# Stop the docker container
	docker-compose kill

clean:
	# Delete the container this stops the container first and then remves it.
	$(MAKE) kill
	docker-compose rm -f

test:
	# Run test cases
	docker-compose run web coverage run manage.py test -v 2

coverage:
	docker-compose run web coverage report -m --omit="*/test*,manage.py,*/settings.py"

code_quality:
	docker-compose run web sh -c "export DJANGO_SETTINGS_MODULE=dodgy_dealership.settings"
	docker-compose run web pylint -d duplicate-code --disable={c0103} --django-settings-module=dodgy_dealership.settings --load-plugins pylint_django listing/
