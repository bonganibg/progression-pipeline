import os
import psycopg2


class PostgresRepository():
    db_name = os.environ.get('DB_NAME')
    user = os.environ.get('DB_USER')
    password = os.environ.get('DB_PASSWORD')
    host = os.environ.get('DB_HOST')
    port = int(os.environ.get('DB_PORT'))

    def __init__(self) -> None:
        self.conn = psycopg2.connect(
                database=self.db_name, user=self.user, password=self.password, 
                host=self.host, port=self.port)

    def get_all(self, table: str, keys: list):        
        with self.conn.cursor() as cur:
            cur.execute(f"SELECT * FROM {table}")
            result = cur.fetchall()
        
        return [
            {
                key: value for key, value in zip(keys, line)
            }
            for line in result            
        ]

    def get(self,table: str, id, keys: str):
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM %s WHERE id = %s", (table, id))
            result = cur.fetchone()

        return {key: value for key, value in zip(keys, result)}
    
    def insert(self, table: str,  data: dict):

        insert_statement = " ".join(
            ["INSERT INTO", 
             table, 
             "(", 
             ", ".join(data.keys()), ")", 
             "VALUES (",
             ", ".join(["%s" for i in data.keys()]),
             ")"
             ]
        )        

        data = tuple(data.values())

        with self.conn.cursor() as cur:
            cur.execute(insert_statement, data)
            
            self.conn.commit()

    def run_query(self, statement: str, data: tuple):
        with self.conn.cursor() as cur:
            cur.execute(statement, data)
            return cur.fetchall()

    def exists(self, table: str, value: str, field: str):
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM %s WHERE %s = %s" % (table, field, value))
            result = cur.fetchone()

        return result is not None
