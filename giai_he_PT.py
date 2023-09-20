#bài này giải hệ phương trình x+2y=5 và 3x+4y =6
# Yêu cầu hoàn chỉnh lại đoạn code
#để có 1 app giải hệ phương trình có n phương trình n ẩn
import numpy as np
A = np.array([(2,2),(3,5)])
B = np.array([5,8])
C  = np.linalg.inv(A) # tạo ma trận nghich đảo
print(A)
print(B)
print(C)
X = np.dot(C,B)
print('Nghiem cua he:',X)
print('Hello nhom 3')
print('abcxyz')
