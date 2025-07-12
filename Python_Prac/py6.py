import numpy as np
# a = np.array([1, 2, 3])
# print(a) 
# a = [1, 2, 3]
# b = [4, 5, 6]
# print(a + b)     # [1, 2, 3, 4, 5, 6] — concatenation
# x = np.array([1, 2, 3])
# y = np.array([4, 5, 6])
# print(x + y)      # [5, 7, 9] — true elementwise addition
# a = np.arange(10, 20)
# print(a)
# #[10 11 12 13 14 15 16 17 18 19]
# print(a[2:5])
# #[12 13 14]
# print(a[::2])  
# #[10 12 14 16 18]
# print(a[::-1])

# a = np.arange(10, 20)
# print(a)
# print(a[8::1]) 
# def mul(x,y):
#     return x*y
# print(mul(5,3))
signal = [1, 0, 1, 0, 1]
pattern = [1, 0, 1]
# print("Signal :", signal)
# print("Pattern:", pattern)

for i in range(len(signal) - len(pattern)+1):
    window = signal[i : i + len(pattern)]
    if np.array_equal(window, pattern):
        print("Pattern found at position:", i)

# def find_pattern(signal, pattern):
#     signal = np.array(signal)
#     pattern = np.array(pattern)
    
    
# positions = find_pattern([1, 0, 1, 0, 1],[1, 0, 1])

# print(positions)
