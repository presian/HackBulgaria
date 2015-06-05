import sqlite3
from Client import Client
from queries import Queries


class Db:

    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.queries = Queries()

    def create_clients_table(self):
        create_query = self.queries.get_query('create_clients_table')
        self.cursor.execute(create_query)

    def change_message(self, new_message, logged_user):
        update_sql = self.queries.get_query('change_message')
        self.cursor.execute(update_sql, (new_message, logged_user.get_id()))
        self.conn.commit()
        logged_user.set_message(new_message)

    def change_pass(self, new_pass, logged_user):
        update_sql = self.queries.get_query('change_pass')
        self.cursor.execute(update_sql, (new_pass, logged_user.get_id()))
        self.conn.commit()

    def register(self, username, password):
        insert_sql = self.queries.get_query('register')
        self.cursor.execute(insert_sql, (username, password))
        self.conn.commit()

    def login(self, username, password):
        select_query = self.queries.get_query('login')

        self.cursor.execute(select_query, (username, password))
        user = self.cursor.fetchone()

        if(user):
            return Client(user[0], user[1], user[2], user[3])
        else:
            return False
