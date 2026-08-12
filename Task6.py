# List — mutable, ordered
grades = ['B', 'A', 'C']
grades.append('A')
grades.sort()
print('List:', grades)
 
# Tuple — immutable, ordered (good for fixed records)
student = ('Ali', 21, 'Computer Science')
print('Tuple:', student)
 
# Set — unordered, unique values only
course_a = {'Ali', 'Sara', 'Bilal', 'Sara'}
course_b = {'Sara', 'Zain', 'Ali'}
print('Union:', course_a | course_b)
print('Intersection:', course_a & course_b)
print('Only in A:', course_a - course_b)
