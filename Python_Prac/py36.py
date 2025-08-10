# # Create list of I and Q values
# # I = [0.1, 0.2, 0.3, 0.4]
# # Q = [0.9, 0.8, 0.7, 0.6]
# # #Print:First sample from I
# # print(I[0])
# # #Print:Last sample from Q
# # print(Q[len(Q)-1])
# # #Print:Third sample from Q
# # print(Q[2])
# # #Print:Total number of samples in I
# # # print(len(I))
# # L = [10, 20, 30, 40, 50, 60]
# # # Index:  0   1   2   3   4   5
# # #        -6 -5  -4  -3  -2  -1
# # print(L[-4: : -1])
# I = [0.1, 0.2, 0.3, 0.4]
# Q = [0.05, 0.15, 0.25, 0.35]
# iq_pair = list(zip(I, Q))
# # print(iq_pair[::-1])
# # print(I[::-1], Q[::-1])
# I_unzip, Q_unzip = zip(*iq_pair)
# print(I_unzip)
# import math
# for i, q in iq_pair:
#     print(math.sqrt(i**2 + q**2))
import math
I=-1
Q=1
theta = math.degrees(math.atan2(Q, I))
print(theta)