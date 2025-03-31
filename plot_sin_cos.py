# 线图基础示例
import matplotlib.pyplot as plt
import numpy as np

# plt.style.use('seaborn-v0_8')

# 设置Matplotlib的字体参数
plt.rcParams['font.family'] = 'stsong' # 选择一个支持中文的字体
plt.rcParams['axes.unicode_minus'] = False # 显示负号

# 生成数据
x = np.linspace(0, 10*np.pi, 10000)

# 创建画布和坐标轴
# plt.figure(figsize=(8, 4))

# 绘制折线图
plt.plot(x, np.sin(x), label='sin(x)')
plt.plot(x, np.cos(x), label='cos(x)')

plt.plot(x, np.sin(x**2), label=r'sin($x^2$)')
plt.plot(x, np.cos(x**2), label=r'cos($x^2$)')

# 添加图表元素
plt.title('三角函数示例')
plt.xlabel('X轴')
plt.ylabel('Y轴')
plt.legend()
# plt.grid(True)

# 显示图表
plt.show()