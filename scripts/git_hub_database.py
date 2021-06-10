import sqlite3
from sqlite3 import Error, OperationalError


class GitHubDatabase():
    def __init__(
        self,
        sqlite_database: str = 'git_hub.db'
    ):
        self.sqlite_database = sqlite_database
        self.conn = None

    def get_connection(self):
        if not self.conn:
            try:
                con = sqlite3.connect(self.sqlite_database)
                self.conn = con
            except Error:
                print(Error)
        return self.conn

    def sql_executor(self, sql_instruction: str):
        cursor = self.get_connection().cursor()
        cursor.execute(sql_instruction)
        self.conn.commit()

    def insert_into_table(
        self,
        table_name: str,
        values: dict
    ):
        sql_instruction = """
            INSERT INTO {table_name}
            VALUES({id}, '{user_name}','{avatar_url}', '{type}', '{url}')
            """.format(
            table_name=table_name,
            id=values.get('id', ''),
            user_name=values.get('login', ''),
            avatar_url=values.get('avatar_url', ''),
            type=values.get('type', ''),
            url=values.get('url', '')
            )

        try:
            self.sql_executor(sql_instruction=sql_instruction)
        except OperationalError:
            sql_table_creation = """
                CREATE TABLE {table_name}(
                    id integer PRIMARI KEY,
                    user_name text,
                    avatar_url text,
                    type text,
                    url text
                )
            """.format(table_name=table_name)
            self.sql_executor(sql_instruction=sql_table_creation)
            self.sql_executor(sql_instruction=sql_instruction)
