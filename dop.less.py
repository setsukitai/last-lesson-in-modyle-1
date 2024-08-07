grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list=sorted(students)
grades_avg={}
for student, grade_num in zip(students_list,grades):
    grades_avg[student]=sum(grade_num)/len(grade_num)
print(grades_avg)