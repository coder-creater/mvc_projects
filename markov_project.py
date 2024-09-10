import numpy as np
import pandas as pd
from scipy.linalg import eig, inv

a = 5
b = a+1
df = pd.read_csv('mpdog.csv')
#df = df.drop(['Probability Chart'], axis=1)
df = df.drop(['Country-Medal'], axis=1)
#df = df.drop(['Country-Medal', '2028','2032','2036', 'Unnamed: 34', '1992.1'], axis=1)

def matrix_cube_root(A, n):
    # Perform eigenvalue decomposition: A = V * D * V^-1
    eigvals, eigvecs = eig(A)
    
    # Take the cube root of the eigenvalues (diagonal matrix D)
    D_cube_root = np.diag((eigvals)**(1/n))
    
    # Reconstruct the matrix cube root: V * D^(1/3) * V^-1
    return np.dot(np.dot(eigvecs, D_cube_root), inv(eigvecs))


# print(df.iloc[:, :16])
input_arr = np.linalg.inv(df.iloc[:, 7:12].to_numpy())
output_arr = df.iloc[:, 8:13].to_numpy()
transition_matrix = output_arr @ input_arr
np.savetxt(f'array{7}s.csv', output_arr @ input_arr, delimiter=',', fmt='%.5f')

# input_arr2 = np.linalg.inv(df.iloc[:, 1:21].to_numpy())
# output_arr2 = df.iloc[:, 2:22].to_numpy()
# transition_matrix2 = output_arr2 @ input_arr2

# transition_matrix = (transition_matrix1 + transition_matrix2)/2
for i in range(8, 12):
    input_arr = np.linalg.inv(df.iloc[:, i:a+i].to_numpy())
    output_arr = df.iloc[:, i+1:b+i].to_numpy()
    np.savetxt(f'array{i}s.csv', output_arr @ input_arr, delimiter=',', fmt='%.5f')
    transition_matrix = transition_matrix @ (output_arr @ input_arr)
    #print(output_arr[:1])

transition_matrix = matrix_cube_root(transition_matrix, 5)
np.savetxt('array.csv', transition_matrix, delimiter=',', fmt='%.5f')

# transition_matrix = df.to_numpy()
state = np.array([[48],[26],[30],[530],[7],[14],[17],[295],[29],[18],[18],[541],[11],[11],[13],[330],[8],[15],[12],[410]])
state2 = np.array([[24],[21],[12],[359],[6],[4],[8],[156],[4],[7],[3],[225],[7],[6],[6],[201],[0],[0],[1],[33]])
state3 = np.array([[36],[39],[37],[588],[9],[8],[8],[332],[19],[13],[19],[313],[7],[16],[20],[323],[14],[15],[17],[433]])
state4 = np.array([[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]])
state4 = df['2012'].to_numpy().reshape(-1, 1)
state5 = np.array([[0.5],[0],[0.667],[0.429],[0]])

transition_matrix_usa = np.array([[0.5, 0, 0.5, 0, 0],[0, 0.25, 0, 0.5, 0.25],[0, 0.083, 0.667, 0.167, 0.083], [0, 0.286, 0.429, 0.286, 0],[1,0,0,0,0]])
transition_matrix_b = np.array([[0.958, 0, 0, 0, 0.042], [0.5, 0.5, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0]])
# print(state4)
# print(transition_matrix[:1])
print(transition_matrix @ state4)
# for i in range(30):
#     state4 = df[df.columns[i]].to_numpy().reshape(-1, 1)
#     print(transition_matrix[:1] @ state4)
# print(np.linalg.matrix_power(transition_matrix, 2) @ state4)
# a1 = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
# a2 = np.array([[2, 3, 11], [5, 6, 11], [8, 9, 12]])
# a1 += a1
# print(a1/2)
# print(np.linalg.inv(a2))
# print(a2 @ np.linalg.inv(a2))
# print(np.linalg.inv(a2) @ a2)