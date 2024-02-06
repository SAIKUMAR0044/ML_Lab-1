#1st question
def number_of_pairs(num_list, target_number):
    count = 0
    for i in range(len(num_list)):
        for j in range(i+1,len(num_list)):
            if num_list[i] + num_list[j] == target_number:
                count += 1
    return count
num_list = [2, 7, 4, 1, 3, 6]
target_number = 10
result = number_of_pairs(num_list, target_number)
print(f"Number of pairs with the sum {target_number} is : {result} pairs")

#2nd question
def calculate(list):
    if len(list) < 3:
        return "Range determination not posiible"
    else:
        return max(list) - min (list)
        
list = [5, 3, 8, 1, 0, 4]
Result = calculate(list)
print(f"The result or range of the numbers is :{Result}")

#3rd question
import numpy as np
def matrix_power(A, m):
    n = len(A)
    if A.shape != (n, n):
        raise ValueError("Matrix A must be square")
    result = np.eye(n)

    while m > 0:
        if m % 2 == 1:
            result = np.dot(result, A)
        A = np.dot(A, A)
        m //= 2

    return result

A = np.array([[1, 2], [3, 4]]) 
m = 2 
result = matrix_power(A, m)
print(f"Result is : {result}")

#4th question
def highest_alphabet_occurrence(input_string):
    char_count = {}
    for char in input_string:
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    maximum_character = max(char_count, key=char_count.get)
    maximum_occurrence = char_count[maximum_character]

    return maximum_character, maximum_occurrence

input_string = "hippopotamus"
result_character, result_occurrence = highest_alphabet_occurrence(input_string)
print(f"The highest occurring character is '{result_character}' with occurrence count {result_occurrence}.")
