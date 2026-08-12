# #Task 1: Celsius to Fahrenheit
# celsius = 25
# fahrenheit = (celsius * 9/5) + 32
# print('Celsius:', celsius, '|', 'Fahrenheit:', fahrenheit)
# print(type(fahrenheit),type(celsius))

# #Task 2:2.	Control Structures — Extend FizzBuzz to run from 1 to 50. In addition to printing Fizz/Buzz/FizzBuzz/the number, count and print how many times 'FizzBuzz' occurred
# fizzbuzz_count = 0
# fizz_count = 0
# buzz_count = 0
# for i in range(1, 51):
#     if i % 3 == 0 and i % 5 == 0:
#         print('FizzBuzz')
#         fizzbuzz_count += 1
#     elif i % 3 == 0:
#         print('Fizz')
#         fizz_count += 1
#     elif i % 5 == 0:
#         print('Buzz')
#         buzz_count += 1
#     else:
#         print(i)
# print('FizzBuzz occurred:', fizzbuzz_count, 'times')
# print('Fizz occurred:', fizz_count, 'times')
# print('Buzz occurred:', buzz_count, 'times')


# #Task 3: 3.	Arrays — Using the array module, store 10 exam scores of your choice. Without using sum() or statistics functions, use a loop to compute and print their average.
# import array
# exam_scores = array.array('f', [85, 92, 78, 96, 88, 91, 84, 89, 93, 87])
# total = 0
# for score in exam_scores:
#     total += score
# average = total / len(exam_scores)
# print('Average exam score:', average)



# #Task 4:4.	NumPy — Create a 4x4 matrix of random integers between 1 and 100 using np.random.randint(). Print the matrix, its transpose, and the sum of each row and column.
# import numpy as np
# matrix = np.random.randint(1, 101, size=(4, 4))
# print('Matrix:\n', matrix)
# print('Transpose:\n', matrix.T)
# print('Row sums:', matrix.sum(axis=1))
# print('Column sums:', matrix.sum(axis=0))

# #Task 5: 5.	Lists, Tuples & Sets — Given two lists of ingredients for two recipes (create your own), find the ingredients common to both, the ingredients unique to each, and a combined shopping list with duplicates removed
# recipe1_ingredients = ['flour', 'sugar', 'eggs', 'butter', 'vanilla extract']
# recipe2_ingredients = ['sugar', 'milk', 'eggs', 'baking powder', 'cocoa powder']

# # Find common ingredients
# common_ingredients = list(set(recipe1_ingredients) & set(recipe2_ingredients))

# # Find unique ingredients for each recipe
# unique_to_recipe1 = list(set(recipe1_ingredients) - set(recipe2_ingredients))
# unique_to_recipe2 = list(set(recipe2_ingredients) - set(recipe1_ingredients))

# # Create a combined shopping list with duplicates removed
# shopping_list = list(set(recipe1_ingredients + recipe2_ingredients))

# print('Common ingredients:', common_ingredients)
# print('Unique to Recipe 1:', unique_to_recipe1)
# print('Unique to Recipe 2:', unique_to_recipe2)
# print('Combined shopping list:', shopping_list)


# #Task 6: 6.	Pandas — Create a small sales dataset (product, quantity, price) as a dictionary, build a DataFrame, add a 'Total' column (quantity × price), save it to a CSV file, then read it back and print the product with the highest total sale.
# import pandas as pd
# sales_data = {
#     'product': ['Product A', 'Product B', 'Product C', 'Product D'],
#     'quantity': [10, 20, 15, 25],
#     'price': [100, 200, 150, 300]
# }
# df = pd.DataFrame(sales_data)
# df['Total'] = df['quantity'] * df['price']
# df.to_csv('sales_data.csv', index=False)
# df_read = pd.read_csv('sales_data.csv')
# highest_sale_product = df_read.loc[df_read['Total'].idxmax()]['product']
# print('Product with the highest total sale:', highest_sale_product)


#Task 7: 7.	Capstone Challenge — Build a mini class gradebook: create a list of 10 student names and a NumPy 10×3 array of quiz scores (3 quizzes per student). Compute each student's average using NumPy, assign a letter grade using control structures (A ≥ 90, B ≥ 80, C ≥ 70, else F), build a Pandas DataFrame with columns Name, Average, and Grade, save it to gradebook.csv, and print only the students who earned an 'A'.
import numpy as np
import pandas as pd
import array

array_of_names = ['Saifullah', 'Mureed', 'Alina', 'Eman', 'Suleman', 'Rashid', 'Marziya', 'Rabia', 'Zainab', 'Bilawal']
quiz_scores = (np.random.randint(50, 101, size=(10, 3))) 

student_averages = np.mean(quiz_scores, axis=1)

# Assign letter grades
grades = []
for avg in student_averages:
    if avg >= 90:
        grades.append('A')
    elif avg >= 80:
        grades.append('B')
    elif avg >= 70:
        grades.append('C')
    else:
        grades.append('F')

# Build DataFrame
df = pd.DataFrame({
    'Name': array_of_names,
    'Average': student_averages,
    'Grade': grades
})

# Save to CSV
df.to_csv('gradebook.csv', index=False)

# Print students who earned an 'A'
a_students = df[df['Grade'] == 'A']
print("Students who earned an 'A':")
print(a_students[['Name']])