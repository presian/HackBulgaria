import requests
from student import Student
from course import Course
from db_mapper import Db
import json


def makeRequestTo(url):
    r = requests.get(url)
    j = json.loads(r.text)
    return j


def makeCourses(courses):
    return [Course(**c) for c in courses]


def parseStudents(json):
    students = [Student(**s) for s in json]
    for s in students:
        s.courses = makeCourses(s.courses)
    return students


def getAllCourses(students):
    result = set()
    for student in students:
        for course in student.courses:
            result.add(course.name)
    return result


def addCoursesToDb(courses, db):
    result = {}
    for course in courses:
        db.add_course(course)
        result[course] = db.cursor.lastrowid
    return result


def addStudentsToSystem(courses_dict, students, db):
    for student in students:
        db.add_student(student.github, student.available, student.name)
        user_id = db.cursor.lastrowid
        for course in student.courses:
            db.add_releation(user_id, courses_dict[course.name], True if course.group == 2 else False)
    db.db.commit()


def main():
    json = makeRequestTo('https://hackbulgaria.com/api/students/')
    students = parseStudents(json)
    courses = getAllCourses(students)
    db = Db()
    courses_dict = addCoursesToDb(courses, db)
    addStudentsToSystem(courses_dict, students, db)


if __name__ == '__main__':
    main()
