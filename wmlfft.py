import numpy as np
from scipy.fft import fft

# 创建一个简单的数组
x = np.array([0.0, 1.0, 0.0, 0.0])

# 计算傅里叶变换
y = fft(x)

# 打印结果
print("输入数组:", x)
print("傅里叶变换结果:", y)
