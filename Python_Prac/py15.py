import numpy as np
iq = np.array([[1, 2],
               [3, 4],
               [5, 6]])

# Rows
print("Row 0:", iq[0])
print("Last row:", iq[-1])
print("Element at row 1, col 0:", iq[1, 0])
print("I channel:", iq[:, 1])

# # # Time-domain signal samples
# S = np.array([1, 0, -1, 0, 1])
# print(S[1:4])
# # print("Manual array:", signal)
# # #t = np.arange(1, 5, 0.1)
# # t = np.linspace(0,1,5)
# # print(t)
# # zeroed = np.zeros(5)
# # ones = np.ones(5)
# # empty = np.empty(5)  # uninitialized values
# # print("Zeros:", zeroed)
# # print("Ones:", ones)
# # zeroed = np.zeros(5)
# # ones = np.ones(5)
# # empty = np.empty(5)  # uninitialized values
# # print("Zeros:", zeroed)
# # print("Ones:", ones)
# # zeroed = np.zeros(5)
# # ones = np.ones(5)
# empty = np.empty(5)  # uninitialized values
# # print("Zeros:", zeroed)
# # print("Ones:", ones)
# # zeroed = np.zeros(5)
# # ones = np.ones(5)
# # empty = np.empty(5)  # uninitialized values
# # print("Zeros:", zeroed)
# # print("Ones:", ones)
# # zeroed = np.zeros(5)
# #ones = np.ones(5)
# empty = np.empty(5)  # uninitialized values
# #print("Zeros:", zeroed)
# print("Empty:", empty)
