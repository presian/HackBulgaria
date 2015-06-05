import sqlite3


class Db:

    def __init__(self):
        self.db = sqlite3.connect('company')
        self.db.row_factory = sqlite3.Row
        self.cursor = self.db.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS
                      employees(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        monthly_salary REAL,
                        yearly_bonus REAL,
                        position TEXT)''')

    def add_employee(self, name, monthly_salary, yearly_bonus, position):
        self.cursor.execute("""INSERT INTO employees(name, monthly_salary, yearly_bonus, position) 
                            VALUES(?, ?, ?, ?)""", (name, monthly_salary, yearly_bonus, position))
        self.db.commit()

    def list_employees(self):
        employees = self.cursor.execute("select * from employees")
        for employee in employees:
            print('Id: {}, Name: {}'.format(employee['id'], employee['name']))

    def monthly_spending(self):
        spend = self.cursor.execute("""SELECT SUM(monthly_salary) FROM employees""")
        return spend.fetchone()[0]

    def yearly_spending(self):
        spend = self.monthly_spending() * 12
        bonus = self.cursor.execute("""SELECT SUM(yearly_bonus) FROM employees""").fetchone()[0]
        return spend + bonus

    # This is not work
    def delete_employee(self, record_id):
        print(record_id)
        self.cursor.execute("""DELETE FROM employees WHERE id = ?""", (record_id,))
        self.db.commit()

    def update_employee(self, record_id, name, monthly_salary, yearly_bonus, position):
        self.cursor.execute("""UPDATE employees
                            SET name = ?, monthly_salary = ?, yearly_bonus = ?, position = ?
                            WHERE id = ?""", (name, monthly_salary, yearly_bonus, position, record_id))
        self.db.commit()


def main():
    db = Db()
    # db.add_employee('Ivan Ivanov', 5000, 10000, 'Software Developer')
    # db.add_employee('Rado Rado', 500, 0, 'Technical Support Intern')
    # db.add_employee('Ivo Ivo', 10000, 100000, 'CEO')
    # db.add_employee('Petar Petrov', 3000, 1000, 'Marketing Manager')
    # db.add_employee('Maria Georgieva', 8000, 10000, 'COO')
    # db.list_employees()
    # print(db.monthly_spending())
    # print(db.yearly_spending())
    # db.update_employee(5, 'Mara Toteva', 88500, 50000, 'Manager')
    db.delete_employee(4)
    db.list_employees()


if __name__ == '__main__':
    main()
