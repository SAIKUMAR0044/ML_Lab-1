#1st question
# Define a function that takes a list of numbers (num_list) and a target sum (target_number)
def number_of_pairs(num_list, target_number):
    # Initialize a counter to keep track of the number of pairs
    count = 0
    
    # Iterate through the indices of num_list using the first loop
    for i in range(len(num_list)):
        # Nested loop to iterate through the indices starting from i+1 to avoid duplicate pairs
        for j in range(i + 1, len(num_list)):
            # Check if the sum of the numbers at indices i and j equals the target_number
            if num_list[i] + num_list[j] == target_number:
                # If true, increment the counter
                count += 1
    
    # Return the final count of pairs
    return count

# Example list of numbers and a target sum
num_list = [3, 4, 8, 9, 2, 5]
target_number = 10

# Call the function with the provided list and target sum
result = number_of_pairs(num_list, target_number)

# Print the result, indicating the number of pairs with the specified sum
print(f"Number of pairs with the sum {target_number} is : {result} pairs")


#2nd question
# Define a function named 'calculate' that takes a list of numbers as input
def calculate(lst):
    # Check if the length of the list is less than 3
    if len(lst) < 3:
        # If true, return a message indicating that range determination is not possible
        return "Range determination not possible"
    else:
        # If the list has 3 or more elements, calculate the range by subtracting the minimum from the maximum
        return max(lst) - min(lst)

# Example list of numbers
lst = [7, 8, 6, 0, 1, 9]

# Call the 'calculate' function with the provided list
result = calculate(lst)

# Print the result, indicating the range of the numbers in the list
print(f"The result or range of the numbers is: {result}")

#3rd question
import numpy as np

# Define a function named 'matrix_power' that calculates the power of a square matrix
def matrix_power(A, m):
    # Get the size of the square matrix A
    n = len(A)
    
    # Check if the matrix A is square
    if A.shape != (n, n):
        raise ValueError("Matrix A must be square")
    
    # Initialize the result matrix as an identity matrix of the same size as A
    result = np.eye(n)

    # Perform matrix exponentiation using the binary exponentiation method
    while m > 0:
        # If the least significant bit of m is 1, multiply the result by A
        if m % 2 == 1:
            result = np.dot(result, A)
        
        # Square the matrix A
        A = np.dot(A, A)
        
        # Right shift m by 1 (equivalent to m //= 2)
        m //= 2

    # Return the final result matrix
    return result

# Example: Create a 2x2 matrix
A = np.array([[2, 1],
              [1, 1]])

# Calculate the matrix power of A to the power of 3
result = matrix_power(A, 3)

# Print the result matrix
print("Matrix A to the power of 3 is:\n", result)


A = np.array([[1, 2], [3, 4]]) 
m = 2 
result = matrix_power(A, m)
print(f"Result is : {result}")

#4th question
# Define a function named 'highest_alphabet_occurrence' that finds the highest occurring alphabet in a given string
def highest_alphabet_occurrence(input_string):
    # Create a dictionary to store the count of each alphabet
    char_count = {}

    # Iterate through each character in the input string
    for char in input_string:
        # Check if the character is an alphabet
        if char.isalpha():
            # Increment the count for the current alphabet in the dictionary
            char_count[char] = char_count.get(char, 0) + 1

    # Find the alphabet with the maximum occurrence using the key argument of the max function
    maximum_character = max(char_count, key=char_count.get)

    # Get the count of the maximum occurring alphabet
    maximum_occurrence = char_count[maximum_character]

    # Return the alphabet and its occurrence count
    return maximum_character, maximum_occurrence

# Example: Input string
input_string = "hippopotamus"

# Call the 'highest_alphabet_occurrence' function with the provided string
result_character, result_occurrence = highest_alphabet_occurrence(input_string)

# Print the result indicating the highest occurring character and its count
print(f"The highest occurring character is '{result_character}' with an occurrence count of {result_occurrence}.")
