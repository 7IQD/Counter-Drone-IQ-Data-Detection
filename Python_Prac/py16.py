import numpy as np
symbols = np.array([1, -1, 1, -1])
print(symbols.shape)
new_symbols = symbols[:, None]
print(new_symbols.shape)


# x = np.array([1, 2, 3, 4]) #1rowx4col
# y = np.array([[10],
#              [20],
#              [30]])        #3rowx1 Col
# print(x.shape, y.shape)    #3rwosX1col

# # t = np.arange(0, 1, 0.1)
# # signal = np.sin(2*np.pi*1*t)
# # print("Time", t)
# # print("Signal:", signal)
# # print("First three samples:", t[:3])
# # print("Every alternate samples:", t[::2])
# arr = np.arange(6)
# print("Original:", arr)
# reshaped = arr.reshape((2,3))
# # Original: [0 1 2 3 4 5] 
# print("Reshaped:", reshaped)
# #Reshaped: [[0 1 2]
# #           [3 4 5]]


