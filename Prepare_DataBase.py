import sqlite3


class SqlDatabase:
    def __init__(self):
        self.hello = "world"

    def create_database(self):
        conn = sqlite3.connect("./SQL/pixel.db")
        curr = conn.cursor()
        curr.execute('''CREATE TABLE IF NOT EXISTS client(
        client_name text,
        client_password text,
        graph_id text,
        graph_name text,
        unit text,
        unit_type text,
        color text
        )''')
        conn.commit()
        conn.close()

    def insert_into_table(self, username, password):
        conn = sqlite3.connect("./SQL/pixel.db")
        curr = conn.cursor()
        curr.execute(f"INSERT INTO client(client_name, client_password) VALUES('{username}', '{password}');")
        conn.commit()
        conn.close()

    def update_table(self, client_name, graph_id, graph_name, unit, unit_type, color):
        conn = sqlite3.connect("./SQL/pixel.db")
        curr = conn.cursor()
        curr.execute(f"UPDATE client "
                     f"SET graph_id = '{graph_id}', graph_name = '{graph_name}',"
                     f"unit = '{unit}', unit_type = '{unit_type}', color = '{color}'"
                     f"WHERE client_name = '{client_name}';")
        conn.commit()
        conn.close()

    def save_in_txt(self, username, password):
        with open("./TXT/current_name.txt", "w") as current:
            current.write(f"{username} \n{password}")
            current.close()

    def read_from_txt(self):
        with open("./TXT/current_name.txt", "r") as variable:
            old_data = variable.readlines()
            variable.close()
        new_data = [item.strip() for item in old_data]
        return new_data

    def display_table_content(self):
        conn = sqlite3.connect("./SQL/pixel.db")
        curr = conn.cursor()
        a = [list(item) for item in curr.execute(f"SELECT * FROM client;")]
        conn.commit()
        conn.close()
        return a

    def clean_database(self):
        conn = sqlite3.connect("./SQL/pixel.db")
        curr = conn.cursor()
        curr.execute(f"DELETE FROM client;")
        conn.commit()
        conn.close()

    def return_wanted_data(self, username, password):
        conn = sqlite3.connect("./SQL/pixel.db")
        curr = conn.cursor()
        data = [list(item) for item in curr.execute(f"SELECT * FROM client;")]
        conn.commit()
        conn.close()
        for item in data:
            if (username in item) and (password in item):
                return item
