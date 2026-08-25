import re

text = """
Contact Geetha at geetha.reddy@gmail.com before 20/08/2026.

For urgent queries, call 9876543210.

Send a copy to student123@klu.ac.in.

The next meeting is on 25/08/2026.
"""

emails = re.findall(r"\S+@\S+", text)

dates = re.findall(r"\d+/\d+/\d+", text)

phones = re.findall(r"\d{10}", text)

print("Emails:")
print(emails)

print()

print("Dates:")
print(dates)

print()

print("Phone Numbers:")
print(phones)