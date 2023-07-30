#!/usr/bin/env python
import cgi
import cgitb
#importing pymysql to establish connection
import pymysql
#enabling the function
cgitb.enable()
# Connect to the database
my_con = pymysql.connect(host='localhost',passwd='password', db='lab8', user='root')
c = my_con.cursor()
#avearge function
def average(midterm_exam1, midterm_exam2, final_exam):
    expression = (midterm_exam1 + midterm_exam2 + 2 * final_exam)
    return expression / 4
#insert record function
def insert(name, midterm_exam1, midterm_exam2, final_exam):
    avg_marks = average(midterm_exam1, midterm_exam2, final_exam)
    with my_con.cursor() as c:
     c.execute("INSERT INTO stud_grade (student_name, midterm_exam1, midterm_exam2, final_exam, avg_marks) VALUES ('{name}', {midterm_exam1}, {midterm_exam2}, {final_exam}, {avg_marks})",
              (name, midterm_exam1, midterm_exam2, final_exam, avg_marks))
# delete the record function delete_record
delete = lambda student_id: c.execute("DELETE FROM stud_grade WHERE id = {student_id}") or my_con.commit()
#display the table record
output_table = lambda: c.execute("SELECT name, avg_marks FROM stud_grade").fetchall()
#Dispalying the table
print(c.fetchall())
form = cgi.FieldStorage()
#inserting the record
data = [form.getvalue(item) for item in ["name", "midterm_exam1", "midterm_exam2", "final_exam"]]
if all(data):
    name, midterm_exam1, midterm_exam2, final_exam = data
    insert(name, midterm_exam1, midterm_exam2, final_exam)
#deleting the record
delete = lambda student_id: delete(int(student_id))
if "delete" in form:
    delete(form.getvalue("delete"))
print("Content-type: text/html; charset= utf-8\n")
print("<html>")
print("<head><title>DATABASE OF STUDENT_GRADES</title></head>")
print("<body>")
print("<h1>LAB8 DATABASE</h1>")
# new student record
form = cgi.FieldStorage()
print("<h2>New Student Record</h2>")
print("""<form action="http://localhost/cgi-bin/lab8.py" method="post">
Name: <input type="text" name="name" value='{}'>.format(form.getvalue("name", ""))>
Midterm Exam 1: <input type="number" name="midterm_exam1" value='{}'>.format(form.getvalue("midterm_exam1", ""))>
Midterm Exam 2: <input type="number" name="midterm_exam2" value='{}'>.format(form.getvalue("midterm_exam2", ""))>
Final Exam: <input type="number" name="final_exam" value='{}'>".format(form.getvalue("final_exam", ""))>
<input type="submit" value="NEW RECORD">
</form>""")
#GRADES OF STUDENTS
print("<h2>Grades of Students</h2>")
print("<h3>GRADES</h3>")
print("<table border='{1}'>")
print("<tr><th>Student Name</th><th>Average Marks</th><th>Delete</th></tr>")
def updation(record):
    name, avg_marks = record
    record_delete = f"http://localhost/cgi-bin/lab8.py?delete={record[0]}"
    return f"<tr><td>{name}</td><td>{avg_marks}</td>" f"<td><a href='{record_delete}'>Delete</a></td></tr>"
for record in output_table:
    print(updation(record))
print("</table>")

print("</body>")
print("</html>")
# Closing the database connection
my_con.close()
# Disabling the cgitb function
cgitb.disable()
