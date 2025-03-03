# Day 6：Python的数据可视化（3学时）

## Matplotlib核心特点与实现原理

```python matplotlib_architecture.py
"""
Matplotlib结构示例伪代码:
Figure 
├─ Canvas (绘图画布)
└─ Axes (坐标系)
    ├─ Axis (坐标轴)
    ├─ Line2D (折线)
    ├─ Text (文本)
    └─ ...其他图形元素
"""
```

### 核心特点

1. **多层抽象架构**
   - **Backend层**：处理底层渲染（Agg/Qt/GTK等）
   - **Artist层**：管理图形元素（线、文本、形状）
   - **Scripting层**：提供pyplot快速绘图API

2. **双模式接口**
   - **MATLAB式**：`plt.plot(x, y)` 快速绘图
   - **面向对象式**：显式控制Figure/Axes对象

3. **丰富的输出支持**

    ```python export_demo.py
    plt.savefig('output.png', dpi=300)  # 支持PNG/SVG/PDF等格式
    ```

4. **可扩展性**
   - 通过`rcParams`全局配置样式
   - 支持LaTeX数学公式渲染

### 实现原理

1. **画布分层结构**
   - **Figure**：顶级容器，对应整个图像文件
   - **Axes**：真实绘图区域，包含坐标轴/刻度等
   - **Axis**：单个坐标轴的数值范围与刻度

2. **渲染引擎流程**

    ```
    用户调用绘图命令 → 创建Artist对象 → 
    Backend将对象转换为底层图形指令 → 
    输出到屏幕/文件
    ```

3. **坐标转换机制**
   - 数据坐标系 → 图像坐标系 → 显示坐标系
   - 支持自定义坐标变换（对数坐标等）

### 集成特性

```python integration.py
# 与Numpy无缝集成
x = np.linspace(0, 2*np.pi)
y = np.sin(x)
plt.plot(x, y)  # 直接绘制numpy数组

# 支持Jupyter内嵌显示
%matplotlib inline  
```

典型应用场景：

- 科研论文图表制作
- 数据探索性分析(EDA)
- 实时数据监控仪表
- GUI应用程序嵌入
- 物理实验：电路特性曲线绘制
- 金融分析：股票K线图绘制
- 气象预测：温湿度等值线图
- 生物信息：基因序列热力图

### 1. 基础绘图功能详解

```python line_plot.py
# 线图基础示例
import matplotlib.pyplot as plt
import numpy as np

# 生成数据
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

# 创建画布和坐标轴
plt.figure(figsize=(8, 4))

# 绘制折线图
plt.plot(x, y, 
         color='blue', 
         linestyle='--',
         linewidth=2,
         marker='o',
         markersize=5,
         label='sin(x)')

# 添加图表元素
plt.title('三角函数示例', fontsize=14)
plt.xlabel('X轴', fontsize=12)
plt.ylabel('Y轴', fontsize=12)
plt.legend()
plt.grid(True)

# 显示图表
plt.show()
```

#### 1.1 基础线图绘制
```python basic_line.py
# 最简绘图示例
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])  # X,Y坐标列表
plt.ylabel('平方值')          
plt.show()
```

#### 1.2 多曲线绘制
```python multi_plot.py
x = np.arange(0, 5, 0.1)
plt.plot(x, x**2, label='Quadratic')    # 二次曲线
plt.plot(x, x**3, label='Cubic')         # 三次曲线
plt.plot(x, 2**x, linestyle=':', label='Exponential')  # 指数曲线
plt.legend(loc='upper left')
```

#### 1.3 散点图绘制
```python scatter_plot.py
# 生成随机数据
np.random.seed(42)
x = np.random.randn(50)
y = x + np.random.normal(0, 0.3, 50)

plt.scatter(x, y, 
            c='red',          # 颜色
            marker='^',       # 点形状
            s=40,            # 点大小
            alpha=0.7,       # 透明度
            edgecolors='black')  # 边缘颜色
            
plt.title('带误差的散点分布', pad=20)
plt.show()
```

#### 1.4 双轴绘图
```python twin_axis.py
# 创建双Y轴系统
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

x = np.arange(1, 11)
ax1.bar(x, height=[20,34,55,12,66,24,55,33,22,15], 
        color='skyblue', 
        alpha=0.7, 
        label='Sales')
ax2.plot(x, [5.2,5.8,6.0,5.5,7.0,6.5,6.8,7.2,7.5,8.0], 
         color='orange', 
         marker='s', 
         label='Growth Rate')

ax1.set_xlabel('Quarter')
ax1.set_ylabel('Sales Volume')
ax2.set_ylabel('Growth Rate (%)')
plt.title('销售数据双轴图表')
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
plt.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
```

技术要点说明：
- `figure()`创建绘图画布，可控制尺寸/dpi参数
- `plot()`默认连接数据点形成折线图
- 颜色支持名称/HEX/RGB格式（如`#ff0000`）
- 线型参数：`'-'`实线、`'--'`虚线、`':'`点线
- `scatter()`支持多维数据可视化，可映射颜色/大小维度
- 双轴绘图适用于单位不同的关联数据对比

## 2. 图表定制功能详解

```python customization.py
import matplotlib.pyplot as plt
import numpy as np

# 基础数据准备
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# 创建绘图对象
plt.figure(figsize=(10, 5), dpi=100)  # 设置画布尺寸和分辨率
```

### 2.1 文本标注定制
```python text_custom.py
plt.title('Trigonometric Functions', 
         fontsize=16,           # 字体大小
         fontweight='bold',     # 字体粗细
         pad=20)                # 标题与图表间距

plt.xlabel('X Axis', 
          fontsize=12, 
          color='navy', 
          labelpad=15)         # 坐标轴标签边距

plt.ylabel('Y Axis', 
          rotation=0,          # 将Y轴标签旋转为水平
          fontsize=12,
          position=(0, 0.95))  # 调整标签位置
```

### 2.2 线条与颜色配置
```python style_custom.py
# 绘制两条曲线并设置样式
plt.plot(x, y1, 
        color='#FF5733',      # 使用HEX颜色代码
        linestyle='--',       # 设置虚线样式
        linewidth=2,          # 线宽
        marker='o',           # 数据点形状
        markersize=6,         # 点大小
        markevery=5,          # 隔5个点显示标记
        alpha=0.8,            # 透明度
        label='Sin(x)')

plt.plot(x, y2, 
        color='steelblue',
        linestyle=':',
        linewidth=3,
        marker='^',
        label='Cos(x)')
```

### 2.3 图例配置
```python legend_custom.py
plt.legend(loc='upper right',      # 设置图例位置
          fontsize=10,            # 字体大小
          title='Function',       # 图例标题
          title_fontsize=12,      # 标题字体大小
          shadow=True,            # 添加阴影
          framealpha=0.8,         # 背景透明度
          edgecolor='black')      # 边框颜色
```

### 2.4 网格与坐标轴
```python axis_custom.py
plt.grid(True, 
        linestyle=':',         # 网格线型
        color='gray', 
        alpha=0.6)            # 网格透明度

plt.axis([0, 10, -1.2, 1.2])  # 显式设置坐标范围[xmin, xmax, ymin, ymax]

plt.xticks(np.arange(0, 11, 2),  # 设置X轴刻度位置
          rotation=45,          # 刻度标签旋转角度
          fontsize=10)

plt.yticks([-1, 0, 1],          # 设置Y轴刻度值
          ['Low', 'Zero', 'High'],  # 对应的标签文字
          fontsize=10)
```

### 2.5 高级定制
```python advanced_custom.py
# 添加文本注释
plt.text(3, 0.8, 'Critical Point', 
        fontsize=12, 
        color='red',
        bbox=dict(facecolor='yellow', alpha=0.5))  # 文本框设置

# 绘制参考线
plt.axhline(y=0, color='black', linestyle='-', linewidth=1)  # 水平辅助线
plt.axvline(x=np.pi, color='green', linestyle='--')  # 垂直辅助线

# 颜色渐变的填充
plt.fill_between(x, y1, y2, 
                where=(y1 > y2),    # 填充条件
                color='skyblue', 
                alpha=0.3, 
                label='Area')
```

# 保存与输出

```python
plt.savefig('custom_plot.png',  # 文件名 
           bbox_inches='tight', # 裁剪多余空白
           dpi=300,            # 输出分辨率
           facecolor='white')  # 背景颜色
plt.show()
```

技术要点：

- `figure()`参数控制画布属性，`dpi`影响输出质量
- RGB颜色支持十六进制格式（`#RRGGBB`）
- 命名字体位置：`'upper right'`/`'lower center'`等组合
- `where`参数可实现条件着色
- `bbox_inches='tight'`自动裁剪多余空白区域

## 3. 子图系统详解

```python subplot_basic.py
import matplotlib.pyplot as plt
import numpy as np

# 创建2x2子图画布
fig, axs = plt.subplots(nrows=2, 
                       ncols=2, 
                       figsize=(10, 8),  # 总画布尺寸
                       sharex=True)     # 共享X轴

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
categories = ['A', 'B', 'C']
values = [25, 40, 33]
axs[1,0].bar(categories, values, color=['red', 'green', 'blue'])

# 第四子图：饼图
sizes = [35, 25, 15, 25]
axs[1,1].pie(sizes, labels=['X', 'Y', 'Z', 'W'], autopct='%1.1f%%')

plt.tight_layout()  # 自动调整子图间距
```

### 3.1 基础子图布局
```python add_subplot.py
# 传统创建方式
fig = plt.figure(figsize=(8, 4))
ax1 = fig.add_subplot(2,2,1)  # 位置参数 (行,列,序号)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,(3,4))  # 合并最后两个单元格

ax1.plot(np.random.rand(10))
ax2.hist(np.random.randn(100), bins=20)
ax3.scatter(np.arange(10), np.arange(10)**2)
```

### 3.2 共享坐标轴
```python shared_axis.py
# 共享坐标轴配置
fig, (ax1, ax2) = plt.subplots(1, 2, 
                              sharey=True,     # 共享Y轴
                              gridspec_kw={'wspace':0.05})  # 调整子图间距

ax1.plot(np.arange(10), np.random.rand(10))
ax2.scatter(np.arange(10), np.random.rand(10))
ax1.set_ylabel('Shared Y Axis')
```

### 3.3 复杂布局
```python gridspec_demo.py
# 使用GridSpec复杂布局
from matplotlib.gridspec import GridSpec

fig = plt.figure(figsize=(12, 6))
gs = GridSpec(3, 3, figure=fig)  # 3行3列网格

# 创建不同形状的子图
ax_main = fig.add_subplot(gs[0:2, 0:2])    # 占据前两行两列
ax_right = fig.add_subplot(gs[0:2, 2])     # 右侧窄列
ax_bottom = fig.add_subplot(gs[2, 0:3])    # 底部整行

# 主图热力图
data = np.random.rand(10,10)
ax_main.imshow(data, cmap='viridis')

# 右图颜色条
plt.colorbar(ax_main.images[0], cax=ax_right)

# 底部柱状图
ax_bottom.bar(np.arange(10), np.random.rand(10))
```

### 3.4 子图嵌套
```python nested_subplot.py
# 主图包含子图
fig = plt.figure()
main_ax = fig.add_subplot(111)
inset_ax = main_ax.inset_axes([0.6, 0.6, 0.35, 0.35])  # [x,y,width,height]

main_ax.plot(np.linspace(0, 20, 100), np.sin(np.linspace(0, 20, 100)))
inset_ax.plot(np.linspace(0, 5, 50), np.cos(np.linspace(0, 5, 50)), color='red')
```

关键参数说明：
- `subplots()`参数：
  - `nrows/ncols`：行列数量
  - `sharex/sharey`：共享坐标轴
  - `constrained_layout`：自动布局优化
- `GridSpec`参数：
  - `width_ratios`/`height_ratios`：行列比例
  - `left`/`right`等：边缘留白控制
- `tight_layout()`相关参数：
  - `pad`：整体边距
  - `wspace/hspace`：子图水平/垂直间距

常见应用场景：
- 多维度数据并行对比
- 训练过程监控面板
- 地理信息多图联动
- 数据-缩略图联合显示

## 4. 图表类型实践

```python bar_chart.py
# 柱状图与分组柱状图
import matplotlib.pyplot as plt
import numpy as np

# 基础柱状图
categories = ['Apple', 'Banana', 'Orange']
sales = [45, 32, 28]
plt.bar(categories, sales, 
       color='skyblue', 
       edgecolor='black',
       width=0.6)

# 分组柱状图示例
x = np.arange(3)  # 生成刻度位置
width = 0.35  # 柱宽

plt.bar(x - width/2, [20, 35, 30], width, label='2022')
plt.bar(x + width/2, [25, 32, 28], width, label='2023')
plt.xticks(x, categories)  # 设置分类标签
```

```python pie_chart.py
# 饼图定制示例
sizes = [35, 25, 20, 20]
labels = ['Action', 'Comedy', 'Drama', 'Sci-Fi']
explode = (0.1, 0, 0, 0)  # 突出显示第一项

plt.pie(sizes, 
       labels=labels,
       autopct='%1.1f%%',  # 显示百分比
       startangle=90,       # 起始角度
       shadow=True,         # 添加阴影
       explode=explode,     # 突出特定扇区
       colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])

plt.axis('equal')  # 保持圆形
```

```python histogram_demo.py
# 直方图（数据分布分析）
data = np.random.normal(170, 10, 250)  # 生成正态分布数据

plt.hist(data, 
        bins=15,              # 分组数量
        color='teal',
        edgecolor='black',    # 边缘线
        alpha=0.7,           # 透明度
        density=True)        # 显示密度曲线

plt.xlabel('Height (cm)')
plt.ylabel('Frequency')
plt.title('Height Distribution')
```

```python scatter_advanced.py
# 高级散点图（多维度可视化）
x = np.random.rand(50)
y = x * 2 + np.random.normal(0, 0.2, 50)
sizes = np.random.randint(10, 200, 50)  # 点尺寸数据
colors = np.random.rand(50)             # 颜色数据

plt.scatter(x, y, 
           s=sizes,        # 尺寸映射
           c=colors,       # 颜色映射
           cmap='viridis', # 颜色方案
           alpha=0.6,      # 透明度
           edgecolors='black')

plt.colorbar(label='Value')  # 添加颜色条
```

```python boxplot_example.py
# 箱线图（数据分布统计）
data = [np.random.normal(0, std, 100) for std in range(1, 4)]

plt.boxplot(data, 
           notch=True,          # 缺口显示中位置信区间
           patch_artist=True,   # 填充颜色
           boxprops=dict(facecolor='lightblue'))

plt.xticks([1, 2, 3], ['Group 1', 'Group 2', 'Group 3'])
plt.ylabel('Measurement')
```

图表类型适用场景：
1. **柱状图**：分类数据对比（如商品销量对比）
2. **饼图**：占比关系可视化（如预算分配）
3. **直方图**：数据分布分析（如考试成绩分布）
4. **散点图**：变量关系研究（如身高体重关系）
5. **箱线图**：数据离群值检测（如质量检测数据）

技术要点：
- 柱状图`width`参数控制不同数据系列间距
- 饼图`autopct='%.1f%%'`自动添加百分比标签
- 直方图`density=True`可显示概率密度曲线
- 散点图`cmap`参数支持多种色谱（viridis, plasma等）
- 箱线图可显示中位数/四分位/离群值等统计特征

## 5. 实战项目：电影数据可视化

### 5.1 数据加载与清洗
```python load_movie_data.py
# 纯Python实现CSV数据加载
import csv
import numpy as np

def load_data(filename):
    """加载清洗后的电影数据"""
    valid_data = []
    with open(filename, encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # 跳过标题行
        
        for row in reader:
            try:
                # 解析年份、评分、类型
                year = int(row[0]) if row[0] else None
                rating = float(row[1])
                genres = row[2].split('|') if row[2] else []
                
                if year and 1900 < year < 2023:  # 数据有效性检查
                    valid_data.append((year, rating, genres))
                    
            except ValueError:
                continue  # 跳过格式错误行
    return valid_data

movie_data = load_data('movies.csv')
ratings = np.array([d[1] for d in movie_data])
```

### 5.2 评分分布直方图
```python rating_histogram.py
import matplotlib.pyplot as plt

plt.figure(figsize=(8,4.5))
plt.hist(ratings, 
        bins=np.arange(0, 10.5, 0.5),  # 每0.5分一个区间
        edgecolor='white',
        color='#2196F3')

plt.title('电影评分分布直方图', fontsize=14)
plt.xlabel('IMDb评分 (0-10分)', fontsize=12)
plt.ylabel('电影数量', fontsize=12)
plt.grid(axis='y', alpha=0.3)
plt.xticks(np.arange(0, 11, 1))
plt.savefig('rating_dist.png')
```

### 5.3 年度趋势折线图
```python year_trend.py
# 统计年产量数据
year_counts = {}
for item in movie_data:
    year = item[0]
    year_counts[year] = year_counts.get(year, 0) + 1

# 转换为排序后的数组
years = np.array(sorted(year_counts.keys()))
counts = np.array([year_counts[y] for y in years])

plt.figure(figsize=(10, 5))
plt.plot(years, counts, 
        marker='o',
        color='#4CAF50',
        linewidth=2)
plt.fill_between(years, counts, color='#C8E6C9', alpha=0.3)
plt.title('2000-2022年电影产量变化趋势', fontsize=14)
plt.xlabel('年份', fontsize=12)
plt.ylabel('年产量', fontsize=12)
plt.grid(linestyle=':')
```

### 5.4 类型分布饼图
```python genre_piechart.py
# 统计类型分布
genre_counter = {}
for item in movie_data:
    for genre in item[2]:
        genre_counter[genre] = genre_counter.get(genre, 0) + 1

# 获取前5大类型
sorted_genres = sorted(genre_counter.items(), key=lambda x: x[1], reverse=True)[:5]
labels = [g[0] for g in sorted_genres]
sizes = [g[1] for g in sorted_genres]
explode = (0.1, 0, 0, 0, 0)  # 突出第一个类别

plt.figure(figsize=(8,8))
plt.pie(sizes, 
       labels=labels,
       autopct='%1.1f%%',
       startangle=90,
       explode=explode,
       shadow=True,
       colors=['#FF5722','#03A9F4','#FFC107','#8BC34A','#9C27B0'])
plt.title('电影类型分布 (Top 5)', fontsize=14)
```

项目实现要点：
1. 数据加载完全使用csv模块实现
2. 数据清洗使用列表解析和异常处理
3. 统计计数使用字典代替Pandas
4. 保存可视化结果为图片文件
5. 输出标准的科研图表格式
