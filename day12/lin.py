lines = [
    "Python is a interpreted language\n",
    "Java is used in most bank applications\n",
    "SQL is also known as RDBMS\n"
]
with open("data.txt", "w") as file:
    file.writelines(lines)
