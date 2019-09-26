# from os import strerror, path
# import traceback
# import sys


class StudentsDataException(Exception):
    def __init__(self, value, msg):
        # super().__init__(value)
        self.value = value
        self.msg = msg
        print(self.value.strerror, self.msg)

    # def myexcepthook(type, value, tb):
    #     msg = ''.join(traceback.format_exception_only(type, value))
    #     print(msg)
    #
    # sys.excepthook = myexcepthook


class BadLine(StudentsDataException):
    def __init__(self, value, msg):
        # super().__init__(value)
        self.value = value
        self.msg = msg
        print(self.value, self.msg)


class FileEmpty(StudentsDataException):
    def __init__(self, value, msg):
        # super().__init__(value)
        self.value = value
        self.msg = msg
        print(self.msg)


def record_line(temp_line):
    temp_word_list = temp_line.split()  # split
    name = temp_word_list[0] + ' ' + temp_word_list[1]
    try:
        if name in students:
            students[name] += float(temp_word_list[2])
        else:
            students[name] = float(temp_word_list[2])
    except Exception as e:
        BadLine(e, "Wrong marks is not added to student sum.")
    # print("Name:", name, "has", temp_word_list[2])


def print_student(students):
    for key in sorted(students.keys()):
        print(key, students[key])


students = {}
# while True:
for i in range(3):
    file_name = input("Please enter file's name: ")
    try:
        fo = open(file_name, "rt")
        for line in fo:
            if len(line) <= 1:
                continue
            record_line(line)
        fo.close()
        break

    except Exception as e:
        StudentsDataException(e, "Try again!")
else:
    print("The number of attempts has been exhausted! Game Over.")
if students:
    print_student(students)
