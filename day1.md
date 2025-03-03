# Day 1：编程环境搭建与基础语法（3学时）

## 1. Python简介与开发环境搭建（Anaconda）

### 1.1 Python核心特性演示

```python features_demo.py
# 动态类型系统演示
variable = 3.1415
print(type(variable))  # 输出: <class 'float'>
variable = "圆周率"
print(type(variable))  # 输出: <class 'str'>

# 多重赋值功能
a, b, c = 1, "two", [3,4,5]
print(f"{a}-{b}-{c}")  # 输出: 1-two-[3, 4, 5]

# 字典推导式示例
squares = {x: x**2 for x in range(5)}
print(squares)  # 输出: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

#### 主要版本特性对比：

| 特性               | Python 3.10+                   | Python 2.7              |
|--------------------|--------------------------------|-------------------------|
| 字符串默认编码      | UTF-8                         | ASCII                   |
| print语法          | 函数形式print()               | 语句形式print           |
| 整除运算符          | 3.10新增模式匹配              | 无                      |

### 1.2 Anaconda安装配置

#### 各平台安装步骤：

**Windows：**

1. 访问[官网](https://www.anaconda.com)下载安装包
2. 双击.exe文件运行安装向导
3. 建议勾选"Add Anaconda to PATH"选项

**macOS：**

```bash install_mac.sh
# 推荐使用Homebrew安装
brew install --cask anaconda
# 配置环境变量
echo 'export PATH="/usr/local/anaconda3/bin:$PATH"' >> ~/.zshrc
```

**Linux：**

```bash install_linux.sh
# 下载安装脚本
wget https://repo.anaconda.com/archive/Anaconda3-2023.09-0-Linux-x86_64.sh
# 运行安装程序
bash Anaconda3-2023.09-0-Linux-x86_64.sh
```

### 1.3 Conda环境管理

```bash conda_env.sh
# 创建新环境
conda create --name ds_env python=3.10

# 激活环境
conda activate ds_env

# 查看已安装包
conda list

# 导出环境配置
conda env export > environment.yml

# 克隆环境
conda create --clone ds_env --name ds_env_backup
```

#### 常用命令速查：

| 功能                   | 命令                                  |
|------------------------|---------------------------------------|
| 搜索包                 | `conda search numpy`                  |
| 安装包                 | `conda install pandas matplotlib`     |
| 更新conda本体          | `conda update -n base conda`          |
| 删除环境               | `conda remove --name old_env --all`   |

### 1.4 开发工具配置

```bash spyder_config.sh
# 安装科学计算全家桶
conda install numpy pandas scikit-learn
```

#### VSCode集成配置：

1. 安装Python扩展插件
2. 选择Anaconda解释器路径（Ctrl+Shift+P → Python: Select Interpreter）
3. 推荐安装的扩展：
   - Pylance（语法检查）
   - Jupyter（笔记本支持）
   - Python Indent（缩进辅助）

### 1.5 环境验证脚本

```python verify_env.py
import sys, platform

print(f"Python版本: {sys.version}")
print(f"操作系统: {platform.system()} {platform.release()}")
print("核心库版本:")
print(f"- NumPy: {np.__version__}") if 'numpy' in sys.modules else None
print(f"- Pandas: {pd.__version__}") if 'pandas' in sys.modules else None

# 输出示例：
"""
Python版本: 3.10.12 | packaged by conda-forge | (main, Jun 23 2023, 22:40:32) [GCC 12.3.0]
操作系统: Linux 5.15.0-78-generic 
核心库版本:
- NumPy: 1.25.2
- Pandas: 2.1.0
"""
```

### 1.6 项目结构规范

```text project_structure/
data_analysis_project/  
├── data/                 # 原始数据
│   ├── raw/             
│   └── processed/       
├── docs/                 # 文档资料
├── notebooks/            # 分析笔记
├── src/                  # 源代码
│   ├── utils/           # 工具函数
│   └── main.py          
├── tests/                # 单元测试
├── environment.yml       # 环境配置
└── README.md             # 项目说明
```

#### 依赖管理示例：

```yaml environment.yml
name: data_analysis
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.10
  - pandas=2.1.0
  - numpy=1.25
  - matplotlib=3.7
  - pip=23.2
  - pip:
    - requests==2.31.0
    - python-dotenv==1.0.0
```

### 1.7 包管理最佳实践

```bash package_management.sh
# 优先使用conda安装
conda install scipy=1.11

# conda未收录的包使用pip
pip install torch torchvision

# 导出精确环境配置
conda list --export > conda_requirements.txt
pip freeze > pip_requirements.txt

# 安装开发模式包
pip install -e .  # 安装当前目录的包
```

#### 注意事项：

1. 避免混合使用conda和pip安装同一包的多个版本
2. conda优先安装来自conda-forge的软件包
3. 复杂环境建议在创建时指定主要依赖版本
4. 定期使用`conda update --all`更新所有包

本配置方案已在以下平台验证通过：

- Windows 11 (64位) with Conda 23.7.4
- Ubuntu 22.04 LTS with Miniconda 23.5.2
- macOS Ventura 13.5 with Anaconda 2023.09
遇到安装问题时可以尝试清除缓存：`conda clean --all -y`

## 2. 变量与数据类型（整型/浮点/字符串/布尔）

### 2.1 基本数据类型表示

```python variables_basic.py
# 整型示例
age = 25                   # 十进制
binary_num = 0b1101        # 二进制 (13)
hex_num = 0x1a             # 十六进制 (26)

# 浮点型示例
price = 3.1415            
sci_num = 2.5e-3          # 0.0025

# 字符串示例
name = "DeepSeek"         
multiline = '''第一行
第二行'''
raw_str = r"换行符:\n不会转义"

# 布尔型示例
is_valid = True           
is_empty = False
```

#### 数据类型特征对比：

| 类型       | 可变性 | 示例            | 说明                    |
|------------|--------|-----------------|-------------------------|
| 整型(int)  | 不可变 | 0b1010 (10进制10)| 任意大整数             |
| 浮点(float)| 不可变 | 3e8 (300000000) | 遵循IEEE754双精度      |
| 字符串(str)| 不可变 | "hello\u00A9"   | 支持Unicode字符        |
| 布尔(bool) | 不可变 | 1 < 2 → True    | bool为int子类          |

### 2.2 变量操作与转换

```python type_operations.py
# 类型转换示例
quantity = "123"
print(int(quantity) + 5)    # 128

pi_str = str(3.1415926)    # "3.1415926"
mix_type = 15 + 3.0        # 自动转换为浮点型

# 浮点精度处理
from decimal import Decimal
precise_float = Decimal('0.1') + Decimal('0.2')

# 布尔转换规则
values = [0, 1, "", "Hello", [], [1]]
print([bool(v) for v in values])  # [False, True, False, True, False, True]
```

#### 转换方法总结：

1. **显式转换**  
   - `int()`：浮点截断取整，有效数字字符串转换  
   - `float()`：支持科学记数法转换  
   - `str()`：所有对象都可转换  
   - `bool()`：0/空值为False，其余为True

### 2.3 字符串格式化操作

```python string_formatting.py
# 多种格式化方式对比
name = "Alice"
age = 28

# 1. % 格式化
print("%s今年%d岁" % (name, age)) 

# 2. format方法
print("{}今年{}岁".format(name, age))

# 3. f-string（Python 3.6+）
print(f"{name.upper()}明年{age+1}岁")

# 4. 模板字符串
from string import Template
t = Template("$name的BMI是$bmi")
print(t.substitute(name=name, bmi=22.5))
```

#### 字符串常用方法：

```python string_methods.py
text = "  Python编程指南  "
print(text.strip())         # 去两端空格 → "Python编程指南"
print(text.split("编"))     # ['  Python', '程指南  ']
print("3.14".isdigit())     # False
print("abc123".isalnum())   # True
print("deepseek".startswith("d"))  # True

# 拼接与重复
header = "=" * 20 + " 菜单 " + "=" * 20
```

### 2.4 数值操作规范

```python numeric_operations.py
# 数值类型验证
assert (5).real == 5, "整型的实部等于自身"
assert isinstance(3+4j, complex), "复数类型检测"

# 安全除法操作
print(7//3)    # 整除 → 2
print(7%3)     # 取模 → 1
print(divmod(7,3))  # (2, 1)

# 数值精度控制
print(0.1 + 0.2 == 0.3)        # False（精度问题）
print(round(2.675, 2))         # 2.67（银行家舍入法）
```

#### 数学运算符优先级（从高到低）：

1. `**`（幂运算）
2. `* / // %` 
3. `+ -`

### 2.5 数据类型验证测试

```python type_validation.py
# 参数类型检查
def calculate_area(radius):
    if not isinstance(radius, (int, float)):
        raise TypeError("必须输入数字类型")
    return 3.1415926 * radius**2

# 字典类型映射
type_map = {
    int: "整数",
    float: "浮点数",
    str: "字符串"
}

sample_data = [10, 3.14, "test", True]
for item in sample_data:
    print(f"值 {item} 类型：{type_map.get(type(item), '其他')}")
# 输出:
# 值 10 类型：整数
# 值 3.14 类型：浮点数
# 值 test 类型：字符串
# 值 True 类型：其他
```

## 3. 输入输出与简单运算（print/input/运算符）

### 3.1 输入输出基础函数

```python basic_io.py
# print基本用法
print("欢迎来到DeepSeek编程世界！")  # 换行输出
print(2024, "人工智能", True)        # 输出多个对象
print(*["A", "B", "C"], sep="-")   # 解包参数：A-B-C

# input接收输入
name = input("请输入姓名：")
print(f"你好，{name}！")

# 数学运算输出
r = float(input("输入圆半径："))
print("周长:", 2 * 3.14159 * r)
print("面积:", 3.14159 * r ** 2)
```

#### 输出格式化控制：

| 参数  | 作用                   | 示例                          |
|-------|------------------------|--------------------------------|
| sep   | 指定分隔符（默认空格） | print(1,2, sep="→") → 1→2     |
| end   | 结尾字符（默认\n）     | print("同一行", end="")        |
| file  | 指定输出目标           | print("错误", file=sys.stderr)|
| flush | 强制刷新缓冲区         | 进度条场景常用                |

### 3.2 类型转换与运算

```python type_conversion.py
# 输入转换示例
age = int(input("年龄："))          # 转为整数
price = float(input("价格："))      # 转为浮点数
valid = bool(input("是否有效："))   # 空字符串转False，其他为True

# 运算优先级演示
result = 5 + 3 * 2 ** 3 // 4       # 等同于5 + ((3 * (2**3)) // 4)
print("计算结果:", result)          # 输出 5 + (24//4) = 11

# 复合赋值运算
count = 10
count += 5       # 等效于count = count + 5
count **= 2      # 现在count = 15^2 = 225
```

#### 运算符优先级表（部分）：

| 优先级 | 运算符                            |
|--------|-----------------------------------|
| 1      | **（幂运算）                     |
| 2      | ~ + -（一元加减和按位取反）      |
| 3      | * / // %（乘除运算）            |
| 4      | + -（加减运算）                 |
| 5      | << >>（位移动）                 |

### 3.3 完整用户交互案例

```python bmi_calculator.py
"""
BMI计算器 v1.0
BMI = 体重kg / (身高m)^2
标准范围：
  低于18.5 → 体重过轻
  18.5-24 → 正常
  25-28 → 过重
  28-32 → 肥胖
"""
print("=" * 20)
height = float(input("输入身高(m)："))
weight = float(input("输入体重(kg)："))

bmi = weight / height**2
print(f"\nBMI计算结果: {bmi:.1f}")  # 保留1位小数

if bmi < 18.5:
    status = "过轻"
elif 18.5 <= bmi < 24:
    status = "正常"
elif 24 <= bmi < 28:
    status = "过重"
else:
    status = "肥胖"

print(f"健康状态: {status}")
```

### 3.4 基础运算演示

```python math_operators.py
# 算术运算符
print(10 + 3)   # 13 → 加法
print(10 - 2.5) # 7.5 → 减法
print(2 ** 4)   # 16 → 幂运算

# 比较运算符
print(5 == 5.0)  # True → 值等判断
print(5 is 5.0)  # False → 类型不同

# 逻辑运算短路特性
result = False and (1/0)  # 不会触发ZeroDivisionError，因为短路
print("安全通过短路测试:", result)
```

#### 特殊数学运算：

```python advanced_math.py
import math

# 绝对值运算
print(abs(-3.14))      # 3.14

# 商余同时获取
print(divmod(35, 6))   # (5, 5)

# 分数运算示例
from fractions import Fraction
half = Fraction(1, 2)
quarter = Fraction(1, 4)
print(half + quarter)  # 3/4

# 数组运算
import numpy as np
arr = np.array([1,2,3])
print(arr * 2)              # [2 4 6]
```

### 3.5 错误处理示例

```python input_validation.py
# 安全数字输入函数
def get_number(prompt, type_=float):
    while True:
        try:
            return type_(input(prompt))
        except ValueError:
            print("输入错误，请重新输入数值")

age = get_number("年龄：", int)
price = get_number("商品价格：")
print(f"总价：{price * 1.1:.2f}")  # 计算含税价格
```

关键要点包括：

1. 输入优先使用类型转换保证数据有效性
2. 复杂运算注意优先级，推荐使用括号明确顺序
3. 格式化输出提升可读性
4. 区分==值比较和is对象身份比较

实际工程中建议在重要计算场景中：

- 使用decimal模块处理精度敏感计算
- 配置静态类型检查工具（mypy）
- 增加异常处理保障程序健壮性

## 4. 课后任务

- 安装Anaconda并完成第一个Python程序

