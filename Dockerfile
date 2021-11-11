FROM python:3.8.10

RUN mkdir -p /app
COPY Pipfile /app
COPY Pipfile.lock /app
WORKDIR /app

RUN apt-get update
RUN pip install --upgrade pip
RUN pip install pipenv
# RUN pipenv shell
RUN pipenv install --deploy --system
ENV DB_HOST postgres-db
ENV PYTHONUNBUFFERED 1
EXPOSE 8081

ENTRYPOINT ["gunicorn", "-b", ":8081"]
CMD ["app.app:create_app()"]
