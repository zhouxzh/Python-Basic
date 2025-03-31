import matplotlib.pyplot as plt
import numpy as np
# 设置Matplotlib的字体参数
plt.rcParams['font.family'] = 'stsong' # 选择一个支持中文的字体
plt.rcParams['axes.unicode_minus'] = False # 显示负号
# 创建2x2子图画布
fig, axs = plt.subplots(nrows=2, 
                       ncols=2, 
                       figsize=(8, 6))  # 总画布尺寸

# 第一子图：折线图
x = np.linspace(0, 10, 100)
axs[0,0].plot(x, np.sin(x))
axs[0,0].set_title('Sin Function')

# 第二子图：散点图
x = np.random.rand(50)
y = x + np.random.normal(0, 0.1, 50)
axs[0,1].scatter(x, y)
axs[0,1].grid(True)

# 第三子图：柱状图
categories = ['苹果', '小米', '红米']
values = [25, 40, 33]
axs[1,0].bar(categories, values, color=['red', 'green', 'blue'])

# 第四子图：饼图
sizes = [35, 25, 15, 25]
axs[1,1].pie(sizes, labels=['春', '夏', '秋', '冬'], autopct='%1.1f%%')

plt.tight_layout()  # 自动调整子图间距
plt.savefig('subplots2x2.png',dpi=300)