import csv
import json

from canvasapi import Canvas
from urllib.request import urlretrieve

# Canvas API URL
API_URL = "https://smu.instructure.com/"
# Canvas Details
with open("canvas-details.json", "r") as file:
    data = json.load(file)
TOKEN = data["Token"]
course_ID = data["Course ID"]
assignment_ID = data["Assignment ID"]

# Initialize Canvas objects
canvas = Canvas(API_URL, TOKEN)
course = canvas.get_course(course_ID)
assignment = course.get_assignment(assignment_ID)

# Get IDs for students
# Get students into dictionary so it is faster to check if student is in dictionary
students_to_grade = {}

# Get students given in csv file
with open("students.csv", "r") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        for name in row:
            students_to_grade[name] = None

# If there are no students provided, get IDs for them all
all_students = course.get_users(enrollment_type=["student"])
if students_to_grade:
    students_to_grade = {
        student.name: student.id
        for student in all_students
        if student.name in students_to_grade
    }
else:
    students_to_grade = {student.name: student.id for student in all_students}

# Download submissions
for student in students_to_grade:
    # Get all attachments from submission and download them
    student_id = students_to_grade[student]
    submission = assignment.get_submission(student_id)
    for attachment in submission.attachments:
        urlretrieve(
            attachment.url,
            f"submissions/{student}.zip",
        )
