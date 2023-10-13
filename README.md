# canvas-submissions-downloader

Python script that downloads student submissions for specified assignment.

## Setup:

1. You need to have the canvas library installed. You can install it using pip:
   - `pip install canvasapi`
2. Create your User-Generated Canvas token:
   1. On your Canvas page, go to _Settings_
   2. Scroll down to _Approved Integrations_
   3. Click the button to create a _New Access Token_
   4. Write the _Purpose_ and select an expiration date and click on _Generate Token_
   5. Copy your newly create token and paste it into the **canvas-details.json** file
3. Write the course ID in the **canvas-details.json** file.
   - The course ID can be found when you are in the home page of the Canvas course. The link follows the following format: `smu.instructure.com/courses/123456`. "123456" would be the course ID.
4. Write the assignment ID in the **canvas-details.json** file.
   - Similarly to the course ID, the assignment ID can also be found in the URL when you navigate into the assignment page. The link follows the following format: `smu.instructure.com/courses/123456/assignments/789012`. "789012" would be the assignment ID.
5. If you want to download the submissions for specific students, add their names in the **students.csv**. Otherwise, the program will download all submissions.
   - It should be one name per row and the names should be exatcly like they appear on Canvas - look at the _People_ page for the course.

<br/><br/>**canvas-details.json** sample:

```
{
   "Token": "892cs~dsk19jcdskl",
   "Course ID": 123456,
   "Assingment ID": "789012"
}
```

### Note:

This program can only download zip files from the submissions as of now. Any other formats will result in an error.
