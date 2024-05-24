grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

student_averages = {}

for i, grades_list in enumerate(grades):
    student_name = list(students)[i]
    average_grade = sum(grades_list) / len(grades_list)
    student_averages[student_name] = average_grade

print(student_averages)