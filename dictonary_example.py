student = [
  {
    'name': 'Jose',
    'school': 'Computing',
    'grades': (66, 77, 88)
  },
  {
    'name': 'oscar',
    'school': 'Computing',
    'grades': (100, 100, 88)
  }
]

def averange_grade(data):
  grades = data['grades']
  return sum(grades) / len(grades)

def averange_grade_all_students(student_list):
  total = 0
  count = 0
  for student in student_list:
    total += sum(student['grades'])
    count += len(student['grades'])
  return total / count

print(averange_grade_all_students(student))