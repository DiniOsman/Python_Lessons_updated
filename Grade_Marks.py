def find_average_marks(marks):
    sum_of_marks = sum(marks)
    total_subjects = len(marks)
    average_marks = sum_of_marks / total_subjects
    return average_marks

def compute_grade(average_marks):
    if average_marks >= 80:
        grade = 'A'
    elif average_marks >= 60:
        grade = 'B'
    elif average_marks >= 50:
        grade = 'C'
    else:
        grade = 'F'
    return grade               
    
    
marks = [60, 55, 70, 80, 75]
average_marks = find_average_marks(marks)
print("Your Average Marks is: ", average_marks)

grade = compute_grade(average_marks)
print("Your Grade is: ", grade)