marks = {
    "Python": 85,
    "Java": 72,
    "DevOps": 90,
    "SQL": 78,
    "Cloud": 88
}

high_marks = {
    subject: mark
    for subject, mark in marks.items()
    if mark >= 80
}

print(high_marks)