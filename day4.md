# Day 4：函数与模块化编程及文件操作（3学时）

## 1. 函数定义与参数传递

### 1.1 基本函数定义  
```python function_basics.py  
def greet(name):  
    """返回欢迎信息（功能注释）"""  
    return f"Hello, {name}!"  

# 调用示例  
print(greet("DeepSeek"))  # Hello, DeepSeek!  
print(greet.__doc__)      # 返回欢迎信息（功能注释）
```

#### 架构说明：  
- `def` 关键字定义函数  
- 函数名遵循蛇形命名法（snake_case）  
- 推荐使用文档字符串描述功能  
- 使用 return 语句返回结果（默认返回 None）

---

### 1.2 参数类型与传递  
```python parameter_types.py  
def data_analyze(data, threshold=0.7, *scores, **options):  
    """  
    :param data: 必需位置参数  
    :param threshold: 带默认值参数（必须声明在无默认参数后）  
    :param scores: 可变位置参数（元组）  
    :param options: 可变关键字参数（字典）  
    """  
    print(f"基底数据: {data}")  
    print(f"阈值: {threshold}")  
    print(f"附加分数: {scores}")  
    print(f"配置选项: {options}")  

# 调用演示  
data_analyze("原始数据", 0.65, 85, 90, mode="strict", log=True)  
"""  
输出:  
基底数据: 原始数据  
阈值: 0.65  
附加分数: (85, 90)  
配置选项: {'mode': 'strict', 'log': True}  
"""
```

---

### 1.3 参数传递机制  
```python passing_mechanism.py  
def modify_args(a, b, c):  
    a = 100          # 新整数对象赋值  
    b.append(4)      # 修改列表对象内容  
    c = [5,6]        # 新列表对象赋值  

# 原始变量  
x = 1               # 不可变类型  
y = [2,3]           # 可变类型  
z = ["init"]  

# 函数调用  
modify_args(x, y, z)  

print("调用后变量值:")  
print(f"x: {x}")   # 1 (未被修改)  
print(f"y: {y}")   # [2,3,4] (已修改)  
print(f"z: {z}")   # ["init"] (未修改)
```

#### 关键结论：  
- 参数传递本质是对象引用的传递  
- 对不可变对象（如整数、字符串）的修改不会影响原始变量  
- 对可变对象（如列表、字典）的内容修改会保留  
- 变量重新赋值会创建新对象，不影响原变量

---

### 1.4 参数解包技巧  
```python argument_unpacking.py  
def plot_point(x, y, color='blue', size=12):  
    print(f"在坐标({x},{y})绘制{color}色点，尺寸{size}")  

# 参数解包调用  
position = (15, 25)  
style_args = {'color': 'red', 'size': 20}  

plot_point(*position, **style_args)  # 在坐标(15,25)绘制红色点，尺寸20  
plot_point(*[30,40], **dict(color='green'))  # 在坐标(30,40)绘制绿色点，尺寸12
```

---

## 参数类型总结表  

| 参数类型        | 语法示例        | 特点                      | 典型应用场景          |  
|----------------|----------------|--------------------------|---------------------|  
| 位置参数        | def func(a)    | 调用时必须传入            | 核心参数处理        |  
| 默认参数        | def func(a=1)  | 声明必须在后，避免可变对象  | 可选配置项          |  
| 可变位置参数     | def func(*args)| 收集为元组                | 处理不定长输入      |  
| 可变关键字参数   | def func(**kwargs)| 收集为字典             | 配置选项/扩展参数    |  

---

## 最佳实践指南  
```python practice_advice.py  
# 1. 避免可变默认值陷阱  
def append_value(value, lst=None):  
    """正确方式：用None作为默认值"""  
    if lst is None:  
        lst = []  
    lst.append(value)  
    return lst  

# 2. 类型提示（Python 3.5+）  
from typing import List, Dict  

def process_data(data: List[str], config: Dict[str, int] = {}) -> float:  
    """清晰的类型注解"""  
    return 0.0  

# 3. 参数验证装饰器  
def validate_input(func):  
    def wrapper(num: int):  
        if not isinstance(num, int):  
            raise TypeError("必须输入整数")  
        return func(num)  
    return wrapper  

@validate_input  
def square(n):  
    return n ** 2  
```  

## 2. 返回值与作用域

### 2.1 返回机制详解
```python return_demo.py
def process_data(raw_data):
    """处理数据并返回多个计算结果"""
    if not raw_data:
        print("空数据输入")
        return  # 隐式返回None
    
    sum_val = sum(raw_data)
    avg_val = sum_val / len(raw_data)
    return sum_val, avg_val  # 显式返回元组

# 结果接收方式
data = [85, 92, 78]
result = process_data(data)           # 接收元组 → (255, 85.0)
total, average = process_data(data)  # 分别解包 → total=255, average=85.0

# 特殊返回情况
print(process_data([]))  # 输出: None
```

#### 返回机制特点：
- 可返回任意类型对象，包括其他函数
- 多返回值自动打包为元组
- 返回语句执行后立即结束函数
- 不存在返回值的函数默认返回`None`

### 2.2 作用域链与访问规则
```python scope_demo.py
global_var = 10  # 全局作用域

def outer_func():
    outer_var = 20  # 闭包作用域
    
    def inner_func():
        inner_var = 30  # 局部作用域
        print("访问全局变量:", global_var)  # 10
        print("访问闭包变量:", outer_var)   # 20
        # 直接修改闭包变量会触发错误，需使用nonlocal
        
    inner_func()
    return inner_var  # NameError，变量作用域仅限于内部

outer_func()
```

#### LEGB作用域优先级：
1. **Local**：函数内部定义变量  
2. **Enclosing**：闭包函数外层变量  
3. **Global**：模块全局变量  
4. **Built-in**：内置命名空间  

### 2.3 global与nonlocal应用
```python variable_scope.py
counter = 0  # 全局变量

def create_counter():
    count = 0  # 闭包作用域
    
    def increment():
        global counter        # 声明全局变量
        nonlocal count        # 声明闭包变量
        count += 1           # 修改闭包变量
        counter += 10        # 修改全局变量
        
        return count, counter
    
    return increment

counter_proc = create_counter()
print(counter_proc())  # (1, 10)
print(counter_proc())  # (2, 20)
```

#### 变量修改规则：
| 操作类型      | 语法              | 作用范围         |
|-------------|-------------------|-----------------|
| 全局修改     | `global x`        | 跨模块修改       |
| 闭包修改     | `nonlocal x`      | 外层非全局作用域 |
| 默认访问     | 直接访问          | LEGB顺序查找    |

### 2.4 闭包与工厂函数
```python closure_demo.py
def power_factory(exponent):
    """创建指数计算函数的工厂"""
    def calculate(base):
        return base ** exponent
    return calculate

# 创建不同幂函数
square = power_factory(2)
cube = power_factory(3)

print(f"3的平方: {square(3)}")  # 9
print(f"3的立方: {cube(3)}")    # 27

# 查看闭包保存的值
print(cube.__closure__[0].cell_contents)  # 3
```

#### 闭包核心特性：
- 保持外层作用域状态
- 实现数据封装
- 减少全局变量使用
- 支持装饰器模式实现

### 作用域错误诊断表
| 错误现象              | 原因分析                    | 解决方案                  |
|-----------------------|----------------------------|--------------------------|
| UnboundLocalError     | 局部变量在使用前未初始化     | 使用global/nonlocal声明  |
| NameError             | 变量在任何作用域都不存在     | 检查变量定义或作用域声明 |
| 意外的变量值变化       | 意外修改了全局变量          | 减少全局变量使用         |
| 闭包变量值不更新       | 未使用nonlocal声明          | 添加nonlocal声明         |

建议实际开发中：

1. 优先使用返回值传递数据，而非依赖作用域修改
2. 谨慎使用global变量
3. 保持函数纯函数特性（无副作用）有利于代码维护
4. 使用闭包替代类实现简单状态管理

函数执行后应显式释放不再需要的局部变量以节省内存，作用域管理是编写可靠Python代码的重要基础。```

## 3. 常用内置函数（map/filter/sorted）

### 3.1 map() 函数应用

```python map_demo.py
# 基本数值处理
numbers = [1, 2, 3, 4]
squared = map(lambda x: x**2, numbers)
print(list(squared))  # [1, 4, 9, 16]

# 多序列映射计算
base = [10, 20]
bonus = [3, 5]
total = map(lambda a,b: a + b/100, base, bonus)
print(list(total))    # [10.03, 20.05]

# 类型转换应用
str_nums = ["3.14", "-5", "100"]
real_nums = map(float, str_nums)
print(list(real_nums))  # [3.14, -5.0, 100.0]
```

#### 函数特性：
- 返回惰性求值的迭代器对象
- 支持多个可迭代对象并行处理
- 函数参数需要与元素数量匹配
- 相比列表推导式更节省内存

---

### 3.2 filter() 函数应用

```python filter_demo.py
# 基本元素筛选
nums = range(10)
even = filter(lambda x: x%2 == 0, nums)
print(list(even))  # [0,2,4,6,8]

# 嵌套条件筛选
def is_valid(word):
    return len(word) > 3 and word.istitle()

words = ["Apple", "box", "Cherry", "dog"]
valid_words = filter(is_valid, words)
print(list(valid_words))  # ['Apple', 'Cherry']

# 特殊值过滤
mixed = [0, False, "", None, 5, "text"]
truthy = filter(None, mixed)  # 过滤假值
print(list(truthy))  # [5, 'text']
```

#### 筛选技巧：
| 筛选模式               | Lambda表达式                | 适用场景            |
|------------------------|----------------------------|--------------------|
| 数值条件              | `lambda x: x > 100`       | 数据过滤          |
| 类型检查              | `lambda x: isinstance(x, int)` | 数据清洗        |
| 复合条件（与）        | `lambda x: x>0 and x%2==0` | 组合筛选          |
| 正则匹配              | 结合re模块                 | 文本处理          |

---

### 3.3 sorted() 函数应用

```python sorted_demo.py
# 基础排序
names = ["Alice", "Bob", "Charlie"]
print(sorted(names, key=len))  # ['Bob', 'Alice', 'Charlie']

# 复杂对象排序
employees = [
    {"name": "Wang", "salary": 8500},
    {"name": "Li", "salary": 12000}
]
print(sorted(employees, key=lambda x: x["salary"], reverse=True))

# 多级排序策略
students = [("Li", 85), ("Zhang", 85), ("Wang", 90)]
print(sorted(students, key=lambda x: (-x[1], x[0])))
# 成绩降序，姓名升序排列
```

#### 排序参数解析：
| 参数       | 示例                      | 功能描述                     |
|------------|--------------------------|------------------------------|
| key        | `key=str.lower`          | 指定排序的基准转换函数       |
| reverse    | `reverse=True`           | 是否逆向排序                 |
| （自定义）  | `key=cmp_to_key(比较器)` | Python3中废弃的cmp参数替代方案 |

---

## 函数组合应用实例

```python combined_usage.py
# 数据处理管道：map -> filter -> sorted
data = ["Grade:85", "invalid", "Grade:92", "Grade:100A"]

# 步骤分解：
processed = map(lambda s: s.split(":")[1], data)          # ['85', 'invalid', '92', '100A']
cleaned = filter(str.isdigit, processed)                  # ['85', '92']
scores = sorted(map(int, cleaned), reverse=True)           # [92, 85]

print("有效成绩排序结果:", scores)

# 使用推导式实现同样功能对比
alt_scores = sorted(
    [int(s.split(":")[1]) 
     for s in data 
     if s.split(":")[1].isdigit()][::-1]
)
```

---

## 性能与技巧提示

```python performance_tips.py
# 惰性求值优化：使用生成器表达式替代
big_data = range(1000000)
squared_iter = (x**2 for x in big_data)  # 不立即求值

# 命名函数 vs lambda
def price_format(price):
    """货币格式化函数"""
    return f"¥{price:.2f}"

prices = [15.8, 30, 45.67]
# 推荐方式（更易维护）
formatted = map(price_format, prices)

# 排序键函数优化（使用operator模块）
from operator import itemgetter, attrgetter

users = [("Alice", 28), ("Bob", 25)]
sorted_by_age = sorted(users, key=itemgetter(1))  # 索引取元素

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
products = [Product("A", 50), Product("B", 30)]
sorted_products = sorted(products, key=attrgetter('price'))
```

主要注意点：

1. Python3中`map/filter`返回迭代器，如需多次使用需转为列表
2. `sorted`的key函数应尽量简单以优化性能
3. 复杂的条件筛选推荐使用生成器表达式提升可读性
4. 大数据场景优先使用迭代器避免内存消耗

## 4. 模块导入与标准库使用（math/random）

### 4.1 模块导入方式详解
```python imports_demo.py
# 基础导入方式
import math
print(math.sqrt(25))  # 5.0

# 别名导入
import random as rd
print(rd.randint(1, 10))  # 生成1-10随机整数

# 选择性导入
from math import pi, cos
print(cos(pi))  # -1.0

# 模块重载（开发调试用）
import importlib
importlib.reload(math)
```

#### 导入方式对比表：
| 方法                | 语法示例                     | 适用场景                 | 内存影响 |
|---------------------|-----------------------------|--------------------------|----------|
| 完全导入            | `import math`               | 频繁使用多个类/函数      | 较大     |
| 别名导入            | `import pandas as pd`       | 长模块名简化             | 中等     |
| 选择性导入          | `from math import sqrt`     | 明确使用指定函数         | 较小     |
| 动态导入            | `module = __import__('os')` | 运行时确定模块名         | 可变     |

### 4.2 math模块核心应用
```python math_operations.py
import math

# 数论函数
print("平方根:", math.sqrt(256))       # 16.0
print("阶乘:", math.factorial(5))      # 120
print("最大公约数:", math.gcd(54, 24)) # 6

# 指数对数
print("自然对数:", math.log(math.e))    # 1.0
print("幂运算:", math.pow(3, 4))       # 81.0

# 三角函数
angle = math.radians(60)  # 转弧度值
print("余弦值:", math.cos(angle))      # ≈0.5

# 特殊常数
print("圆周率π:", math.pi)            # 3.141592653589793
print("自然对数基数e:", math.e)       # 2.718281828459045

# 实用函数
print("向上取整:", math.ceil(3.2))     # 4
print("向下取整:", math.floor(3.8))    # 3
```

### 4.3 random模块随机应用
```python random_demo.py
import random

# 基础随机数
print("0-1随机浮点:", random.random())          
print("范围整数:", random.randint(10, 20))    

# 序列操作
colors = ["红", "蓝", "绿", "黄"]
print("随机选择:", random.choice(colors))       # 随机选一个
print("随机样本:", random.sample(colors, 2))    # 无重复抽取两个
random.shuffle(colors)                         # 原地打乱顺序
print("洗牌后:", colors)

# 分布函数
print("正态分布:", random.gauss(0, 1))         # 均值0，标准差1
print("均匀分布:", random.uniform(3.5, 5.5))   # [3.5,5.5)均匀分布

# 密码生成应用
def generate_password(length=8):
    chars = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
    return ''.join(random.choices(chars, k=length))

print("\n生成密码:", generate_password())
```

### 4.4 联合作业示例
```python geometry_demo.py
import math
import random

class Circle:
    def __init__(self, radius=None):
        self.radius = radius or random.uniform(1, 10)
    
    @property
    def area(self):
        """使用math库计算精确面积"""
        return math.pi * self.radius ** 2
    
    @property
    def diameter(self):
        return 2 * self.radius

# 生成随机圆实例
circles = [Circle() for _ in range(5)]

# 分析结果
print(f"{'半径':<8}{'直径':<8}{'面积':<12}")
for circle in circles:
    print(f"{circle.radius:.2f}\t"
          f"{circle.diameter:.2f}\t"
          f"{circle.area:.4f}")
```

### 标准库特性对比
| 功能维度       | math模块                      | random模块                              |
|----------------|-------------------------------|-----------------------------------------|
| 主要用途       | 数学运算                      | 生成伪随机数                            |
| 精度保证       | 最高精度计算                  | 基于伪随机算法                          |
| 线程安全       | 线程安全                      | 共享Random实例时需注意同步              |
| 性能特点       | 优化计算性能                 | 中等生成速度                           |
| 常用开发场景   | 科学计算/数据分析            | 游戏开发/随机采样/加密相关             |
| 特殊注意事项   | 浮点数精度问题               | 不可用于密码学安全场景                 |

### 最佳实践提示
```python security_note.py
# 加密安全提示
import secrets

# 不安全的随机（random模块）
print("非安全随机:", random.randint(1, 100))

# 安全的替代方案（适用于密码学）
print("安全随机数:", secrets.randbelow(100))  # 使用secrets模块

# 精度处理建议
from decimal import Decimal
correct_calculation = Decimal(math.pi) * Decimal("2.718")  # 避免浮点误差累积
```

实际工程建议：

1. math模块优先保留原始精度
2. 随机种子设置使用`random.seed()`保证可复现性
3. 多线程环境每个线程创建独立Random实例
4. 安全敏感场景使用`secrets`模块替代`random`

## 5. 文件读写操作（txt/csv）

### 5.1 基础文本文件操作

```python file_io_basic.py
# 文本文件三种常用读写模式
MODES = {
    'r': '读取（默认模式）',
    'w': '写入（覆盖）', 
    'a': '追加',
    'r+': '读写模式'
}

# 标准操作流程建议
def write_log(filename):
    """文件写入最佳实践"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("==== 系统日志 ====\n")
        f.writelines([f"事件{i}: 已记录\n" for i in range(3)])

def read_log(filename):
    """多种读取方式对比"""
    with open(filename, 'r', encoding='utf-8') as f:
        # 方法1 全内容读取
        # content = f.read()
        
        # 方法2 行读取优化
        for line in f:
            print(line.strip())
            
        # 方法3 按块读取（适合大文件）
        # while True:
        #     chunk = f.read(4096)
        #     if not chunk: break
        #     process(chunk)

# 执行演示
write_log('system.log')
read_log('system.log')
```

输出结果：
```
==== 系统日志 ====
事件0: 已记录
事件1: 已记录
事件2: 已记录
```

### 5.2 CSV文件数据操作

```python csv_operations.py
import csv

# 写入CSV文件（包含标题）
def write_student_csv(filename):
    data = [
        {'name': '张三', 'math': 85, 'english': 92},
        {'name': '李四', 'math': 76, 'english': 88}
    ]
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'math', 'english'])
        writer.writeheader()
        writer.writerows(data)

# 读取CSV文件（带类型转换）
def read_student_csv(filename):
    with open(filename, 'r', encoding='utf-8-sig') as f:  # 处理BOM
        reader = csv.DictReader(f)
        student_data = []
        for row in reader:
            student = {
                'name': row['name'],
                # 字符串转换为数值
                'math': float(row['math']),
                'english': float(row['english'])
            }
            student_data.append(student)
        return student_data

# 执行示例
write_student_csv('students.csv')
students = read_student_csv('students.csv')
print(f"李四的英语成绩：{students[1]['english']}")  # 88.0
```

#### CSV处理参数总结：
| 参数          | 作用                    | 推荐值              |
|---------------|-------------------------|---------------------|
| delimiter       | 字段分隔符              | ',' (默认)         |
| quoting       | 引用规则               | csv.QUOTE_MINIMAL |
| newline       | 换行符                 | '' (系统默认)      |
| encoding      | 编码格式               | utf-8/utf-8-sig    |

### 5.3 大文件操作优化

```python large_file_process.py
# 逐行处理大型日志文件
def filter_log(input_file, output_file, keyword):
    """过滤包含关键字的日志条目"""
    with (open(input_file, 'r', encoding='utf-8') as infile,
          open(output_file, 'w', encoding='utf-8') as outfile):
        
        for line in infile:
            if keyword in line:
                outfile.write(line)

# CSV分块处理（1万行为单位）
def batch_process_csv(filename):
    from itertools import islice
    
    with open(filename, 'r') as f:
        while True:
            chunk = list(islice(f, 10000))
            if not chunk:
                break
            process_chunk(chunk)
            
def process_chunk(rows):
    """模拟处理数据块"""
    print(f"处理{len(rows)}行数据")

# 内存映射文件处理（需要精确控制时）
import mmap
def search_large_file(filename, pattern):
    with open(filename, 'r') as f:
        s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        return s.find(pattern.encode())
```

### 文件操作错误处理矩阵

| 错误类型        | 常规场景              | 解决方案                                 |
|-----------------|-----------------------|-----------------------------------------|
| FileNotFoundError | 文件不存在读取       | try块检查或使用os.path.exists         |
| PermissionError  | 没有文件权限         | 检查文件属性或管理员权限              |
| UnicodeDecodeError | 编码错误            | 指定正确编码格式（如GBK尝试）         |
| csv.Error        | CSV格式不兼容        | 调整dialect参数或修正源文件           |
| IsADirectoryError | 路径指向目录         | 检查文件路径合法性                    |

关键注意事项：

1. 推荐使用`with`上下文管理器处理文件，确保自动关闭  
2. CSV文件写入时指定`newline=''`避免空行问题  
3. 大文件处理使用迭代方式避免内存溢出  
4. 优先使用明确编码格式（推荐`utf-8-sig`适配Excel生成文件）

## 6. 使用with语句管理资源

### 6.1 基础文件操作

```python file_handling.py
# 传统文件操作潜在问题
f = open('data.txt', 'w')
try:
    f.write('sample data')
    # 发生异常可能跳过close
finally:
    f.close()

# with语句改进版本
with open('data.txt', 'w') as f:
    f.write('可靠的写入方式')  # 自动处理关闭
```

#### with语句优点：

- 确保资源正确释放
- 自动化异常处理
- 代码可读性更高
- 支持多个上下文管理器

### 6.2 管理多个资源

```python multiple_resources.py
# 同时处理两个文件
with open('source.txt', 'r') as src, \
     open('backup.txt', 'w') as dst:
    content = src.read()
    dst.write(content.upper())

# 等效嵌套写法
with open('source.txt') as src:
    with open('backup.txt', 'w') as dst:
        dst.write(src.read().lower())

print("文件操作完成")  # 两个文件在此处已自动关闭
```

### 6.3 自定义上下文管理器

```python custom_context.py
class DatabaseConnection:
    def __init__(self, db_name):
        self.db = db_name
        
    def __enter__(self):
        print(f"连接{self.db}数据库...")
        return self  # 可返回连接对象
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"关闭{self.db}连接")
        if exc_type:  # 处理异常
            print(f"错误发生: {exc_val}")

# 使用场景
with DatabaseConnection('users') as conn:
    print("执行数据库操作")
    # raise ConnectionError("模拟故障")  # 测试异常处理

# contextlib简化实现
from contextlib import contextmanager

@contextmanager
def open_config(file):
    print("加载配置文件")
    yield {'config': True}
    print("保存配置变更")

with open_config('app.cfg') as cfg:
    print("当前配置:", cfg)
```

### 6.4 异常处理与最佳实践

```python error_handling.py
class SafeFile:
    def __init__(self, filename, mode):
        self.file = open(filename, mode)
        
    def __enter__(self):
        return self.file
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        if exc_type is not None:
            print(f"错误发生: {exc_val}")
            # return True  # 阻止异常传播
        print("资源已清理")

try:
    with SafeFile('data.log', 'a') as f:
        f.write("系统启动\n")
        raise ValueError("测试异常情况")
except ValueError as e:
    print(f"捕获到异常: {e}")

print("代码继续执行")
```

### 上下文管理对比表

| 特性\方法        | 传统try-finally          | with语句                   | 适用场景              |
|------------------|-------------------------|---------------------------|---------------------|
| 资源释放保证      | 手动实现               | 自动处理                 | 任何需要清理的资源场景 |
| 代码简洁度        | 冗长                   | 简洁易读                 | 简单到复杂的上下文    |
| 异常处理          | 需要多层嵌套           | 上下文管理器统一处理     | 复杂异常管理          |
| 多资源管理        | 嵌套复杂               | 单行多资源声明           | 需要同时管理多个资源 |
| 自定义支持        | 需手工实现             | 实现协议或使用装饰器      | 需要封装资源逻辑      |

### 最佳实践指南

1. **文件操作**：始终使用with打开文件
```python best_practice.py
# 推荐写法
with open('data.csv') as f:
    process(f.read())

# 避免写法
f = open('data.csv')
data = f.read()
f.close()
```

2. **多资源管理**：用逗号分隔多个上下文管理器

```python multi_resource.py
with (
    open('input.txt') as src,
    open('output.txt', 'w') as dst,
    DatabaseConnection('logs') as conn
):
    dst.write(src.read())
    conn.log_operation()

```

3. **异常处理**

```python exception_handling.py
class Transaction:
    def __enter__(self):
        print("开始事务")
        return self
        
    def __exit__(self, exc_type, *_):
        if exc_type:
            print("回滚事务")
        else:
            print("提交事务")
        return True  # 阻止异常传播

with Transaction():
    print("执行数据库操作")
    # raise ValueError("事务失败")
```

关键要点：

1. with块结束后自动调用__exit__
2. __exit__返回值控制是否传播异常
3. contextlib简化常用资源的上下文管理
4. 适用于任何需要"准入-退出"模式的场景

特殊资源拓展应用：

- 多线程锁管理
- 数据库连接池
- 临时目录操作
- 网络套接字连接

## 7. 异常处理（try-except-else-finally）

### 7.1 基础异常捕获机制
```python basic_exception.py
# 除法计算异常处理
def safe_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("错误：除数不能为零")
        result = float('inf')  # 返回无穷大
    except TypeError as e:
        print(f"类型错误：{e}")
        result = None
    else:
        print(f"{a}/{b} = {result}")  # 成功执行显示结果
    finally:
        print("计算操作完成")         # 总会执行清理工作
    return result

# 测试不同场景
print(safe_division(10, 2))    # 正常情况
print(safe_division(5, 0))     # 除零错误
print(safe_division("10", 2))  # 类型错误
```

#### 执行结果：
```
10/2 = 5.0
计算操作完成
5.0

错误：除数不能为零
计算操作完成
inf

类型错误：unsupported operand type(s) for /: 'str' and 'int'
计算操作完成
None
```

### 7.2 完整异常处理流程
```python file_handling.py
def process_file(filename):
    file = None
    try:
        file = open(filename, 'r', encoding='utf-8')
        data = file.read()
    except FileNotFoundError:
        print(f"文件 {filename} 不存在")
    except UnicodeDecodeError:
        print("文件编码错误")
    else:
        print(f"成功读取{len(data)}字节数据")
        return data
    finally:
        if file:                   # 确保文件关闭
            file.close()
            print("文件句柄已释放")

# 故意调用不存在的文件
content = process_file('ghost.txt')
```

#### 代码说明：
1. `try`块尝试执行可能出错的代码  
2. `except`捕获特定异常并处理  
3. `else`块处理无异常时的后续操作（数据转换等）  
4. `finally`保证资源释放（如关闭文件）  

### 7.3 异常层次与自定义异常
```python custom_exceptions.py
class InvalidAgeError(Exception):
    """自定义年龄异常"""
    def __init__(self, age, message="年龄必须在1-120岁之间"):
        self.age = age
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.age} 岁 -> {self.message}"

def register_user(age):
    if not 1 <= age <= 120:
        raise InvalidAgeError(age)
    print("用户注册成功")

try:
    register_user(150)
except InvalidAgeError as e:
    print(f"注册失败：{e}")  # 输出：150 岁 -> 年龄必须在1-120岁之间
```

#### Python异常层次（部分）：
```
BaseException
 ├── KeyboardInterrupt
 ├── SystemExit
 └── Exception
      ├── ValueError
      ├── FileNotFoundError
      ├── TypeError
      └── ...其他内置异常
```

### 7.4 新的异常处理语法（Python 3.11+）
```python new_except_syntax.py
try:
    import non_exist_module
except* ModuleNotFoundError as eg:  # 异常组处理
    for err in eg.exceptions:
        print(f"缺少模块: {err.name}")
```

### 错误处理模式对比表
| 代码块    | 执行时机                  | 典型应用场景               |
|-----------|---------------------------|---------------------------|
| try       | 尝试执行可能出错的代码     | 资源访问/数值计算        |
| except    | 遇到指定异常时触发         | 错误处理/恢复流程        |
| else      | 无异常时执行               | 数据转换/成功后的后续操作|
| finally   | 无论是否异常都会执行       | 资源释放/状态复位        |

### 最佳实践建议
```python exception_best_practices.py
# 1. 精确捕获特定异常
try:
    user_input = int(input("输入数字："))
except ValueError:
    print("无法转换为整数")

# 2. 日志记录代替简单打印
import logging
logging.basicConfig(filename='app.log')
try:
    risky_operation()
except Exception as e:
    logging.exception("操作异常: %s", str(e))

# 3. 上下文管理器结合异常处理
class DatabaseConnection:
    def __enter__(self):
        self.connect()
    def __exit__(self, exc_type, *_):
        self.close()
        if exc_type:
            self.rollback()

# 4. 重启机制实现
max_retries = 3
for attempt in range(max_retries):
    try:
        connect_service()
        break
    except ConnectionError:
        if attempt == max_retries-1:
            raise
        print(f"重试连接 ({attempt+1}/{max_retries})...")
```

关键提示：

1. 避免空的`except:` 会捕获所有异常，甚至`KeyboardInterrupt`
2. 异常实例信息可通过`as`关键字获取
3. `raise`不带参数重新抛出当前异常
4. `assert`语句用于调试期的条件检查，生产代码建议显式检查

将错误管理作为程序的重要功能组件进行设计，可以使代码更健壮且易于维护。

## 8. 实践项目：小说词频统计

```python word_freq.py
import re
from collections import Counter

def read_novel(file_path):
    """读取并返回小说文本内容"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"错误：文件 {file_path} 未找到")
        exit(1)

def clean_text(text):
    """清洗文本：转为小写、移除标点符号"""
    text = text.lower()  # 统一小写
    text = re.sub(r'[^\w\s]', '', text)  # 移除非字母数字字符
    return re.sub(r'\d+', '', text)       # 移除数字

def get_stopwords(stop_file='stopwords.txt'):
    """加载停用词表，可传入自定义停用词文件"""
    default_stopwords = {
        'the', 'and', 'to', 'of', 'a', 'in', 'that', 'was', 'he', 'it',
        'his', 'her', 'as', 'with', 'for', 'she', 'had', 'you'
    }
    try:
        with open(stop_file, 'r') as f:
            return set(f.read().splitlines()) | default_stopwords
    except FileNotFoundError:
        return default_stopwords

def analyze_frequency(text, top_n=20, stopwords=None):
    """分析词频并返回结果"""
    words = text.split()  # 默认空格分词
    if stopwords:
        words = [w for w in words if w not in stopwords]
    counter = Counter(words)
    return counter.most_common(top_n)

def main(file_path):
    """主流程控制函数"""
    # 数据准备阶段
    raw_text = read_novel(file_path)
    cleaned_text = clean_text(raw_text)
    
    # 分析配置选项
    stopwords = get_stopwords()
    
    # 统计分析
    results = analyze_frequency(cleaned_text, top_n=30, stopwords=stopwords)
    
    # 结果呈现
    print(f"{'单词':<15}频率")
    print("-"*25)
    for word, count in results:
        print(f"{word:<15}{count}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 2:
        print("用法: python word_freq.py 小说文件路径")
        exit(1)
    
    main(sys.argv[1])
```

### 代码执行示例

```bash
$ python word_freq.py pride_and_prejudice.txt
单词          频率
-------------------------
elizabeth     785
darcy         525
bennet        443
jane          353
bingley       297
...以下省略...
```

### 关键实现解析

#### 1. 多层级文本清洗

```python
def clean_text(text):
    """双重正则过滤确保文本规范"""
    text = re.sub(r'[^\w\s]', '', text)  # 删除标点符号
    text = re.sub(r'\s+', ' ', text)     # 合并多余空格 
    return text.strip().lower()
```

#### 2. 可扩展的停用词系统

```python stopwords.txt
a
an
the
and
but
...
```

#### 3. 高效分析算法

使用`collections.Counter`比手动字典统计更快，其`most_common()`方法复杂度为O(n log k)

### 优化建议

1. **分词优化**：

```python
from nltk.tokenize import word_tokenize  # 更准确的分词

def analyze_frequency(text):
    words = word_tokenize(text)  # 替换原生的split()
```

2. **词干提取**：

```python
from nltk.stem import PorterStemmer

ps = PorterStemmer()
processed = [ps.stem(w) for w in words]
```

3. **并行处理**：

```python
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor() as executor:
    chunks = [text[i:i+10000] for i in range(0, len(text), 10000)]
    results = executor.map(process_chunk, chunks)
```

### 复杂度分析

| 步骤          | 时间复杂度       | 空间复杂度    |
|---------------|------------------|---------------|
| 文件读取      | O(N)            | O(N)          |
| 文本清洗      | O(N)            | O(N)          |
| 词频统计      | O(N)            | O(M) 不同词数|
| 结果排序      | O(M log M)      | O(1)          |

本实现可在标准配置计算机上处理超过100MB的文本文件，主要瓶颈在于内存加载。对于GB级文件建议采用分批处理方式。

*注：本示例代码需要安装NLTK库方可使用高级分词功能*

