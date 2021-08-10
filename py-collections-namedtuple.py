from collections import namedtuple

if __name__ == '__main__':
    total_student = int(input())
    column_names = list(input().split())
    Student = namedtuple('Student', column_names)

    total_marks = 0
    for i in range(total_student):
        s = Student(*input().split())
        total_marks += int(s.MARKS)
    print(total_marks/total_student)
