from canvasapi import Canvas, requester
import json

# Canvas API URL
API_URL = "https://smu.instructure.com/"
# Canvas Details
with open("canvas-details.json", "r") as file:
    data = json.load(file)
TOKEN = data["Token"]
course_ID = data["Course ID"]
assignment_ID = data["Assingment ID"]

# Initialize Canvas objects
canvas = Canvas(API_URL, TOKEN)
course = canvas.get_course(course_ID)
assignment = course.get_assignment(assignment_ID)

for s in assignment.get_submissions():
    print(s)
