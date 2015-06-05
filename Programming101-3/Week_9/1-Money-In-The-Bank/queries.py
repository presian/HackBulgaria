class Queries:

    def __init__(self):
        self.__queries = {
            'create_clients_table': """CREATE TABLE IF NOT EXISTS
                            clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username TEXT,
                            password TEXT,
                            balance REAL DEFAULT 0,
                            message TEXT)""",
            'change_message': """UPDATE clients
                            SET message = ?
                            WHERE id = ?""",
            'change_pass': """UPDATE clients
                            SET password = ?
                            WHERE id = ?""",
            'register': """INSERT INTO clients (username, password)
                            VALUES (?, ?)""",
            'login': """SELECT
                            id,
                            username,
                            balance,
                            message
                        FROM clients
                        WHERE username = ?
                            AND password = ?
                        LIMIT 1"""
        }

    def get_query(self, name):
        return self.__queries[name]
