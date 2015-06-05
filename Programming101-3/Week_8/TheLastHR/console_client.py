from db_mapper import Db

db = Db()
exit = False
while not exit:
    try:
        command = int(input("""
            \n1.List all students with their GitHub accounts.
            \n2.List all courses
            \n3.List all students and for each student - list the courses he has been attending.
            \n4.Find the students that have attented the most courses in Hack Bulgaria.
            \n5.Exit
            \n
            \n==========================
            \nPlease enter a command:"""))
        if command == 1:
            objects = db.listAllStudentsWithGitHub()
            for o in objects:
                print('Name: {} -> GitHub: {}'.format(o['name'], o['github']))
        elif command == 2:
            rows = db.listAllCourses()
            for r in rows:
                print('Course: {}'.format(r['name']))
        elif command == 3:
            students = db.listAllStudentsWithTheirCourses()
            result = {}
            for student in students:
                if student['name'] in result and student['course'] is not None:
                    result[student['name']].append(student['course'])
                else:
                    result[student['name']] = []
                    if student['course'] is not None:
                        result[student['name']].append(student['course'])
            for key, value in result.items():
                print("Name: {}, Courses: {}".format(key, value))
        elif command == 4:
            students_as_rows = db.listTopThenStudentsWithMostCourses()
            print('asd')
            for s in students_as_rows:
                print("Name:{}, Courses count: {}".format(s['name'], s['count']))
        elif command == 5:
            exit = True
    except:
        print("Your command is invalid! Please try again!")
