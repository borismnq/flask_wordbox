from app.database.database import Database
from datetime import datetime

def test_create_user(app):
    db_obj = Database()
    user_json = dict()
    user_json['name'] = "example name"
    user_json['last_name'] = "example lastname"
    user_json['phones_array'] = [144444,5555111,223123]
    user_json['creation_date'] = str(datetime.now().date())
    user_id = db_obj.create_user(user_json)
    
    assert user_id is not None