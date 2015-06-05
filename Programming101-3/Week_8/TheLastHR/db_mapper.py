import sqlite3


class Db:

    def __init__(self):
        self.db = sqlite3.connect('hack_bulgaria')
        self.db.row_factory = sqlite3.Row
        self.cursor = self.db.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('PRAGMA foreign_keys = ON')
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS
                      students(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        github TEXT,
                        name TEXT,
                        available BOOLEAN)""")
        self.db.commit()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS
                      courses(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT)""")
        self.db.commit()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS
                      students_courses(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        student_id INTEGER,
                        course_id INTEGER,
                        evening_group BOOLEAN,
                        FOREIGN KEY(student_id) REFERENCES students(id),
                        FOREIGN KEY(course_id) REFERENCES courses(id))""")
        self.db.commit()

    def add_student(self, github, available, name):
        self.cursor.execute("""INSERT INTO students(github, available, name)
                            VALUES(?, ?, ?)""", (github, available, name))

    def add_all_students(self, query_values):
        # print("""INSERT INTO students(github, available, name) VALUES """ + query_values)
        self.cursor.execute("""INSERT INTO students(github, available, name) VALUES ?""", (query_values,))
        self.db.commit()

    def add_course(self, name):
        self.cursor.execute("""INSERT INTO courses(name)
                            VALUES(?)""", (name,))
        self.db.commit()

    def add_releation(self, student_id, course_id, evening_group):
        self.cursor.execute(
            """INSERT INTO students_courses(student_id, course_id, evening_group)
            VALUES(?, ?, ?)""", (student_id, course_id, evening_group))

    def listAllStudentsWithGitHub(self):
        return self.cursor.execute("""SELECT
                                    id,
                                    name,
                                    github
                                FROM students""").fetchall()

    def listAllStudentsWithTheirCourses(self):
        return self.cursor.execute("""SELECT
                                        s.id,
                                        s.name,
                                        c.name AS course
                                    FROM students s
                                    LEFT JOIN students_courses sc
                                    ON s.id = student_id
                                    LEFT JOIN courses c
                                    ON sc.course_id = c.id""").fetchall()

    def listTopThenStudentsWithMostCourses(self):
        return self.cursor.execute("""SELECT
                                            s.name,
                                            count(s.id) AS count
                                        FROM students s
                                        LEFT JOIN students_courses sc
                                        ON s.id = student_id
                                        LEFT JOIN courses c
                                        ON sc.course_id = c.id
                                        GROUP BY s.id
                                        ORDER BY count DESC
                                        LIMIT 10""").fetchall()

    def listAllCourses(self):
        return self.cursor.execute("""SELECT
                                            name
                                        FROM courses""").fetchall()
