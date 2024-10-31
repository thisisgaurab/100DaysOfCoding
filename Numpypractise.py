import numpy as np

# Q1: Create a 1D NumPy array containing the numbers from 0 to 9.
arr1 = np.arange(0, 10)

# Q2: Given the array created in Q1, multiply each element by 2.
arr2= arr1*2

# Q3: Reshape the array from Q2 into a 2D array with 2 rows and 5 columns.
arr3 = arr2.reshape((2, 5))

# Q4: From the reshaped array in Q3, extract the second row.
ar4r = arr3[1]

# Q5: Calculate the mean and standard deviation of the array created in Q1.
mean_value = np.mean(arr1)
std_value = np.std(arr1)

# Q6: Using the array from Q1, create a boolean mask that identifies which elements are greater than 5.
boolean_mask = arr1 > 5

# Q7: Use the boolean mask from Q6 to filter out elements from the original array that are greater than 5.
filter_array = arr1[boolean_mask]
print(filter_array)

# Q8: Create a second 1D array containing numbers from 10 to 19. Stack this array vertically with the reshaped array from Q3.
second_arr = np.arange(10, 20).reshape(2, 5)
result_arr = np.vstack((arr3, second_arr))
print(result_arr)

# Q9: Calculate the sum of each column in the stacked array from Q8.
col_sum = np.sum(result_arr, axis = 0)
print(col_sum)

# Q10: Create a 2D array representing a 2x2 matrix [[1, 2], [3, 4]] and compute its determinant.
arr10 = np.array([[1, 2], [3, 4]])
det = np.linalg.det(arr10)

# Q11: Create a 1D array of shape (3,) containing the values [1, 2, 3]. Add this array to a 2D array [[10], [20], [30]].
# What will be the result?

arr11 = np.array([1,2, 3])
arr_2d =  np.array([[10], [20], [30]])
result = arr11 + arr_2d
print(result)

# Q12: Create a 3x3 identity matrix and replace the diagonal elements with [5, 5, 5].
identity_matrix = np.eye(3)
np.fill_diagonal(identity_matrix, 5)
print(identity_matrix)

# Q13: Save the array from Q1 to a CSV file and then load it back into a new NumPy array.
np.savetxt('arr1.csv', arr1, delimiter=',')
load_arr = np.loadtxt('arr1.csv', delimiter=',')
print(load_arr)

# Q14: Write a function that takes a 1D NumPy array and returns the number of even and odd numbers.
def count_num(arr):
    even_count = np.sum(arr%2==0)
    odd_count = np.sum(arr%2!=0)

    return even_count, odd_count
even_num, odd_num = count_num(arr1)
print(f'Even count is: {even_num}, Odd Count is: {odd_num}')

# Q15: Given a random 2D array of shape (5, 5), find the indices of the maximum value in the array.
arr15 = np.random.rand(5, 5)
index = np.unravel_index(arr15.argmax(), arr15.shape)
print(arr15)
print(index)







