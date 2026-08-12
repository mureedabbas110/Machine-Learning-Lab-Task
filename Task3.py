score = 95
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
else:
    grade = 'F'
print('Grade:', grade)
 
total = 0
for n in range(1, 11):
    total += n
print('Sum 1-10:', total)
 
countdown = 5
while countdown > 0:
    print(countdown)
    countdown -= 1
print('Liftoff!')
