age = 21                # int
gpa = 3.75              # float
name = 'Ayesha'         # str
is_enrolled = True      # bool
advisor = None          # NoneType
 
print(type(age), type(gpa), type(name), type(is_enrolled), type(advisor))
 
# type casting
age_str = str(age)
gpa_int = int(gpa)      # truncates to 3
print(age_str, type(age_str))
print(gpa_int, type(gpa_int))
