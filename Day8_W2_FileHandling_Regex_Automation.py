#************FILE HANDLING - TEXT FILES*****************

# Step 1: Write data into file.txt
with open('file.txt', 'a') as f:
    f.write("Name: Atqa\n")
    f.write("Age: 19\n")
    f.write("Skills: Python, Data Analysis, ML\n")
    f.write("Hobbies: Reading, Coding, Music\n")

# Read from the file 
with open('file.txt', 'r') as f:
    data= f.read()
    print(f"****All content in file**** \n{data}")

# Read line by line
with open ('file.txt', 'r') as f:
    print ("****Data line by line****")
    for line in f:
        print (line.strip())

#Append in file
with open ('file.txt', 'a') as f:
    print ("****Append data in file****\n")
    f.write("Country: Pakistan\n")

# Replace word and Update file
with open ('file.txt', 'r') as f:
    mydata=f.read()
mydata=mydata.replace('Atqa', 'Atqa Asma')
with open ('file.txt', 'w') as f:
    f.write(mydata)
print (f"Data changed is {mydata}")

# Modify line by line
with open ('practice.txt', 'r') as f:
    lines= f.readlines()

for i in range(0,2):
    if i<len(lines):
     lines[i]=lines[i].upper()
    
with open('practice.txt', 'w') as f:
    f.writelines(lines)


# Find word in specific line
keyword = "Age"
with open('file.txt', 'r') as f:
    for line in f:
        if keyword in line:
            print("Found:", line.strip())

# Count word, char, lines
with open('practice.txt', 'r') as f:
    text = f.read()
word_count = len(text.split())
char_count = len(text)
line_count = text.count('\n') + 1
print("Words:", word_count, "Chars:", char_count, "Lines:", line_count)


#************FILE HANDLING -JSON FILES*****************
#Read and write in JSON file
data = {
    "name": "Atqa",
    "age": 21,
    "skills": ["Python", "MongoDB", "React"]
}
import json
with open ('data.json', 'w') as f:
    json_string=json.dump(data,f, indent=4)
    print(json_string)
with open ('data.json', 'r') as f:
    data=json.load(f)
data['age']=19
with open ('data.json', 'w') as f:
    json.dump(data,f,indent=4)
print(data['skills'])


#***************FILE HANDLING -CSV FILES******************
#Reading and Writing with CSV Files
import csv
students= [
    [id, 'name' , 'age'],
    [1, "Atqa", 19],
    [2, "Ahmed", 20]
]

with open ('mycsv.csv' , 'w', newline="") as f:
    writer=csv.writer(f)
    writer.writerows(students)

with open('mycsv.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

#Reading and Writing with DictWriter, DictReader
import csv

students = [
    {"id": 1, "name": "Atqa", "age": 21},
    {"id": 2, "name": "Ahmed", "age": 22}
]

with open('students.csv', 'w', newline='') as f:
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students)
import csv

with open('students.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['name']} is {row['age']} years old.")


#Modifying csv data
import csv

with open('students.csv', 'r') as f:
    reader = csv.DictReader(f)
    students = list(reader)

for student in students:
    if student['name'] == 'Atqa':
        student['age'] = '22'

with open('students.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['id', 'name', 'age'])
    writer.writeheader()
    writer.writerows(students)

# **************Regex Expression***************
import re

text = """
Contact us at support@example.com or sales@company.org.
You can also call 0345-1234567 or 0300-9876543.
Visit our website: https://www.example.com/about-us.
"""

# 1. Extract emails
emails = re.findall(r"[\w\.-]+@[\w\.-]+\.\w+", text)

# 2. Extract phone numbers
phones = re.findall(r"03\d{2}-\d{7}", text)

# 3. Extract domains
domains = re.findall(r"https?://(?:www\.)?([\w\-]+\.\w+)", text)

print("Emails:", emails)
print("Phones:", phones)
print("Domains:", domains)

# **************Automation***************
import os
print (os.getcwd())
print(os.listdir())
os.mkdir("new_folder")#creayte new folder
os.rename("new_folder", "old_folder")#remame folder
os.rmdir("old_folder")#delete empty folder

import shutil
shutil.copyfile('students.csv', 'copy_student.csv')
shutil.move('copy_student.csv', 'new_folder\copy_student.csv')
shutil.rmtree("new_folder")

import glob
txt_files = glob.glob("*.txt")
print(txt_files)
py_files = glob.glob("**/*.py", recursive=True)
print(py_files)

import time
def slow_function():
    time.sleep(2)  # Simulates a slow task (waits 2 seconds)

start = time.time()
slow_function()
end = time.time()

print(f"Execution Time: {end - start:.2f} seconds")

#Use of time Profiling
import time
start = time.time()
for i in range(500):
    print(i)
end = time.time()
print(f"Execution Time: {end - start:.4f} seconds")

#Use of Decorators
def greet_decorator(func):
    def wrapper():
        print("Hello!")
        func()
        print("Goodbye!")
    return wrapper
@greet_decorator
def say_name():
    print("My name is Atqa.")
say_name()

# # Two Sum
def two_sum_brute(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
print (two_sum_brute([1,2,3,4]),3)

# # Valid Palindrom
import re
def is_palindrome(s):
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return s == s[::-1] 
print(is_palindrome("12344321"))
print(is_palindrome("12345541"))
