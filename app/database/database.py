import psycopg2

from app.database.config import ConfigDatabase

class Database(ConfigDatabase):
    def __init__(self) -> None:
        conn = psycopg2.connect(**self.postgres_access)
        cursor = conn.cursor()
        query = f'''CREATE TABLE IF NOT EXISTS {self.table_name}(
                    user_id SERIAL PRIMARY KEY NOT NULL,
                    name varchar(150) NOT NULL,
                    last_name varchar(150) NOT NULL,
                    phones_array integer ARRAY,
                    creation_date date NOT NULL)'''
        cursor.execute(query)
        cursor.close()
        conn.commit()
        

    def get_user_by_id(self, user_id):
        conn = psycopg2.connect(**self.postgres_access)
        cursor = conn.cursor()
        select_query = f"select * from {self.table_name} where user_id = '{user_id}';"
        cursor.execute(select_query)
        data = cursor.fetchone()
        cursor.close()
        conn.commit()
        return data
    
    
    def create_user(self, user_json):
        try:
            conn = psycopg2.connect(**self.postgres_access)
            cursor = conn.cursor()
            query = f"INSERT INTO {self.table_name}" \
                            "(name, last_name, phones_array, creation_date)" \
                            f"VALUES('{user_json['name']}', '{user_json['last_name']}', '{set(user_json['phones_array'])}', '{user_json['creation_date']}');"

            cursor.execute(query)
            cursor.execute('SELECT LASTVAL()')
            id = cursor.fetchone()[0]
            cursor.close()
            conn.commit()
            
        except Exception as e:
            print(e)
        return id
