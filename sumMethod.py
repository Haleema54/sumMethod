'''

8) Write a program to get tuple elements in a single line separated by spaces and print the sum of the elements without using sum() method.
Sample Input:
10 20 30
Sample Output:
60
program:
# Input: Read the tuple values as a single line of space-separated integers
tuple_values = tuple(map(int, input().split()))

# Initialize a variable to hold the sum
total_sum = 0

# Calculate the sum by iterating over the tuple
for value in tuple_values:
    total_sum += value

# Output: Print the total sum
print(total_sum)
'''
