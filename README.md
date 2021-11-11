# Install and run
- pip install pipenv
- pipenv shell
- pipenv install
- pipenv gunicorn -b :8081 "app.app:create_app()"

# Dockercompose run

- docker-compose up

# Run tests
- Change 'host' value on database.ini file from 'postgresdb' to 'localhost'
- pipenv run pytest