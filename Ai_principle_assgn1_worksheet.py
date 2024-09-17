import numpy as np

# Assuming you have your arrays named array_3x3 and array_1x3

# Create sample arrays (replace these with your actual arrays)
array_3x3 = np.random.random((7, 3, 3))
array_1x3 = np.random.random((7, 1, 3))

# Iterate over each pair of corresponding matrices
for i in range(len(array_3x3)):
    # Extract the second matrix from array_1x3
    second_matrix = array_1x3[i, 0]
    
    # Pad the second matrix with zeros to match the shape of the first matrix in array_3x3
    padded_matrix = np.vstack((array_3x3[i, 0], second_matrix))
    
    # Assign the padded matrix to the first matrix in array_3x3
    array_3x3[i, 0] = padded_matrix

print("Modified array_3x3:")
print(array_3x3)


