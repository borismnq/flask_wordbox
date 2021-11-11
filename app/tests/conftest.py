import pytest
from app.app import create_app
from datetime import datetime
from app.database.database import Database

@pytest.fixture(scope="session")
def app():
    _app = create_app()
    _app.testing = True

    return _app

@pytest.fixture(scope="function")
def add_user():
    def _add_user(name, last_name, phones_array):
        db_obj = Database()
        user_json = dict()
        user_json['name'] = name
        user_json['last_name'] = last_name
        user_json['phones_array'] = phones_array
        user_json['creation_date'] = str(datetime.now().date())
        user_id = db_obj.create_user(user_json)
        return user_id
    return _add_user
