from datetime import datetime

class Student:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name

    def request_session(self, tutor, course, requested_time):
        if course not in self.course_name:
            print("You are not enrolled in this course")
            return None

        if course not in tutor.course_name:
            print("This tutor does not teach this course.")
            return None

        session = TutoringSession(self, tutor, course, requested_time)

        print ("Tutoring session requested :)")
        return session

class Tutor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name

class TutoringSession:
    def __init__(self, student, tutor, course, requested_time):
        self.student = student
        self.tutor = tutor
        self.course = course
        self.requested_time = requested_time
        self.status = "Pending"

    def display_session(self):
        print("\n--- Tutoring Session ---")
        print("Student:", self.student.name)
        print("Tutor:", self.tutor.name)
        print("Course:", self.course)
        print("Requested Time:", self.requested_time)
        print("Status:", self.status)

student1 = Student("StudentName", ["CS311", "CS370"])

tutor1 = Tutor("TutorName", ["CS370", "CS170"])

requested_time = datetime(2026, 11, 2, 13, 0)

session1 = student1.request_session(
    tutor1, "CS370", requested_time
)

if session1:
    session1.display_session()
