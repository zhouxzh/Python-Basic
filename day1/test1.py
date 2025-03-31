import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
# 创建模拟课堂数据
data = {
    '姓名': ['张三', '李四', '王五', '赵六', '陈七'],
    '出勤次数': [18, 20, 15, 19, 17],
    '作业得分': [88, 92, 85, 90, 87],
    '课堂参与': [9, 10, 7, 8, 8],
    '期末成绩': [85, 95, 78, 88, 82]
}

# 创建DataFrame
df = pd.DataFrame(data)

# 添加综合表现指标（加权平均）
df['综合表现'] = df['出勤次数']*0.2 + df['作业得分']*0.3 + df['课堂参与']*0.2 + df['期末成绩']*0.3

# 创建画布和子图
fig, axs = plt.subplots(2, 2, figsize=(15, 12))

# 绘制出勤情况条形图
axs[0,0].bar(df['姓名'], df['出勤次数'], color='skyblue')
axs[0,0].set_title('出勤情况（总次数20）')
axs[0,0].set_ylim(0, 20)

# 绘制作业得分折线图
axs[0,1].plot(df['姓名'], df['作业得分'], 'go-', linewidth=2, markersize=8)
axs[0,1].set_title('作业得分趋势')
axs[0,1].set_ylim(70, 100)

# 绘制期末成绩分布饼图
axs[1,0].pie(df['期末成绩'], labels=df['姓名'], autopct='%1.1f%%',
           colors=['gold', 'lightcoral', 'lightgreen', 'lightskyblue', 'violet'])
axs[1,0].set_title('期末成绩分布')

# 绘制综合表现雷达图
categories = ['出勤', '作业', '参与', '期末']
N = len(categories)
angles = np.linspace(0, 2*np.pi, N, endpoint=False).tolist()

for index, row in df.iterrows():
    values = [
        row['出勤次数']/20*100,
        row['作业得分'],
        row['课堂参与']*10,  # 参与分数换算为百分制
        row['期末成绩']
    ]
    # 闭合雷达图
    values += values[:1]
    angles_ = angles + angles[:1]

    axs[1,1].plot(angles_, values, 'o-', linewidth=2,
                label=row['姓名'])
    axs[1,1].fill(angles_, values, alpha=0.25)

axs[1,1].set_title('综合表现雷达图')
axs[1,1].set_xticks(angles)
axs[1,1].set_xticklabels(categories)
axs[1,1].legend(loc='upper right')

plt.tight_layout()
plt.savefig('student_performance.pdf', dpi=300, bbox_inches='tight')
