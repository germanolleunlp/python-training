from statistics import mean


def calculate_average_grades(assignments):
    grades = {}

    for assignment in assignments:
        student = assignment.student.name
        try:
            grades[student]
        except KeyError:
            grades[student] = []
        finally:
            grades[student].append(assignment.grade)

    for student in grades:
        grades[student] = mean(grades[student])

    return grades
