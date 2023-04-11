import psycopg2
import env


class DB():
    def __init__(self):
        self.connect()

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                    dbname=env.DB_NAME,
                    user=env.DB_USER,
                    host=env.DB_HOST,
                    password=env.DB_PASS)
        except psycopg2.DatabaseError as e:
            print(e)

    def run(self, sql="", params=[]):
        self.conn.cursor().execute(sql, params)
        self.conn.commit()

    def get(self, sql="", params=[]):
        cur = self.conn.cursor()
        cur.execute(sql, params)
        return cur.fetchall()

    def __del__(self):
        self.conn.close()
