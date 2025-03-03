# **Day 2：Python程序控制基础（3学时）**

## 分支结构详解

### 单分支if结构应用场景

适用场景：当只需要处理条件成立的情况时使用

```python
# 示例：年龄验证
age = 20
if age >= 18:
    print("您已成年，可以进入！")
```

### 双分支if-else结构执行流程

执行流程：条件成立执行if代码块，否则执行else代码块

```python
# 示例：奇偶判断
num = 15
if num % 2 == 0:
    print(f"{num}是偶数")
else:
    print(f"{num}是奇数")
```

### 多分支if-elif-else嵌套规则

规则说明：

1. 按从上到下的顺序检查条件
2. 第一个满足条件的代码块将被执行
3. elif可以有多个，else可选
4. 使用缩进定义代码块范围

```python
# 示例：成绩等级评定
score = 85
if score >= 90:
    print("A")
elif 80 <= score < 90:
    print("B")
elif 70 <= score < 80:
    print("C")
else:
    print("D")

# 嵌套示例：用户登录验证
username = "admin"
password = "123456"

if username == "admin":
    if password == "123456":
        print("登录成功！")
    else:
        print("密码错误")
else:
    print("用户名不存在")
```

### 条件表达式与短路运算原理

#### 条件表达式（三元运算）

语法：`结果 = 值1 if 条件 else 值2`

```python
# 示例：返回较大值
a, b = 10, 20
max_value = a if a > b else b
```

#### 短路运算原理

逻辑运算符执行规则：

- 在 `and` 运算中，如果前项为False，直接返回False不检查后项
- 在 `or` 运算中，如果前项为True，直接返回True不检查后项

```python
# 短路运算示例
def check_list(lst):
    return len(lst) > 0 and lst[0] == "Python"

# 当传入空列表时不会触发索引错误，因为len(lst) > 0为False导致直接返回False
print(check_list([]))  # 安全地返回False
```

## 2. 循环结构深度解析

### 2.1 for循环工作机制及迭代协议

Python的for循环基于迭代协议实现，通过调用可迭代对象的`__iter__()`方法获取迭代器，然后不断调用迭代器的`__next__()`方法获取值。

```python iteration_protocol.py
class FibonacciGenerator:
    """自定义斐波那契数列迭代器"""
    def __init__(self, max_count):
        self.max = max_count
        self.count = 0
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max:
            raise StopIteration
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return result

print("斐波那契数列迭代演示:")
for num in FibonacciGenerator(5):
    print(num, end=' ')  # 输出：0 1 1 2 3

# 等效的底层实现机制
print("\n\n手动迭代演示:")
iterator = iter(FibonacciGenerator(3))
while True:
    try:
        print(next(iterator), end=' ')  # 输出：0 1 1
    except StopIteration:
        break
```

#### 关键特点：

- `iter()`函数调用对象的`__iter__()`方法
- `next()`函数触发`__next__()`方法执行
- `StopIteration`异常由迭代器主动抛出

### 2.2 序列类型遍历技巧

Python提供多种便捷的遍历工具：

```python traversal_techniques.py
colors = ['red', 'green', 'blue']
hex_codes = ['#FF0000', '#00FF00', '#0000FF']

# 带索引遍历（常规写法 vs 优化写法）
print("索引遍历对比:")
# 传统方式
for i in range(len(colors)):
    print(f"{i}: {colors[i]}")

# 改进方式（避免使用len()）
for index, color in enumerate(colors, start=10):
    print(f"{index}-{color}")  # 索引从10开始

# 并行遍历多个序列
print("\n多序列遍历:")
for color, code in zip(colors, hex_codes):
    print(f"{color.center(10)} -> {code}")

# 字典遍历最佳实践
print("\n字典遍历:")
inventory = {'apples': 25, 'oranges': 18}
for item, quantity in inventory.items():
    print(f"商品：{item.upper()}，库存：{quantity:+}")
```

#### 遍历优化技巧：

- 使用反向迭代器`reversed()`逆向遍历序列
- 嵌套结构使用`itertools.product`代替多重循环
- 迭代器切片使用`itertools.islice`

### 2.3 range()函数参数模式详解

range函数支持三种参数组合：

```python range_demo.py
# 单参数模式（停止值）
print("range(5):\t", list(range(5)))        # [0,1,2,3,4]

# 双参数模式（起始，停止）
print("range(3,7):\t", list(range(3,7)))    # [3,4,5,6]

# 三参数模式（起始，停止，步长）
print("range(10,0,-2):", list(range(10,0,-2)))  # [10,8,6,4,2]

# 常见应用场景
print("\n应用场景:")
# 生成等差数列
step_sequence = [x * 0.5 for x in range(0, 5)] # 0.0,0.5,1.0,...2.0

# 创建索引映射字典
index_map = {k:v for v,k in enumerate(reversed(range(10)))}

# 生成网格坐标
grid = [(x,y) for y in range(5) for x in range(5)]
```

#### 特殊模式说明：

- 负步长时起始值必须大于结束值
- 浮点数步长推荐使用`numpy.arange()`
- 内存优化：range对象不存储完整列表

### 2.4 循环控制关键词深度应用

控制流关键词显著提升循环灵活性：

```python control_flow.py
# break应用：数据有效性校验
print("数值有效性验证:")
valid_numbers = []
while True:
    value = input("输入数值（q退出）: ")
    if value.lower() == 'q':
        break
    if not value.isdigit():
        print("无效输入！")
        continue
    valid_numbers.append(int(value))
    print(f"最新队列：{valid_numbers}")

# 带有else的循环结构
print("\n素数检测优化:")
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            print(f"找到因数 {i}")
            break
    else:
        return True
    return False

print("127是素数吗？", is_prime(127))

# continue的高级应用：跳过复合条件
print("\n复杂跳过逻辑:")
for num in range(100):
    if num % 3 == 0 or num % 5 == 1:
        continue
    if num > 50:
        break
    print(num, end=' ')
```

#### 控制流规范：
1. **break使用准则**
   - 最多跳出当前循环层
   - 常用在搜索场景（找到即退出）
2. **continue适用场景**
   - 预处理时过滤无效数据
   - 跳过不需要处理的边界条件
3. **else扩展模式**
   - while...else常用于重试机制
   - 可与异常处理结合形成安全验证

### 高级循环范式

```python advanced_patterns.py
# 循环中的状态保持
def sliding_window(items, size=3):
    """滑动窗口生成器"""
    return (items[i:i+size] for i in range(len(items)-size+1))

# 无限循环模式（需设计合理退出条件）
import time
def status_monitor(interval=1):
    """系统状态监测"""
    while True:
        # 获取系统状态的伪代码
        status = check_system_status()  
        if status == 'ERROR':
            print("检测到系统错误！")
            break
        time.sleep(interval)

# 并行迭代与条件判断的混合应用
matrix = [[1,2,3], [4,5,6], [7,8,9]]
if any(10 in row for row in matrix):
    print("矩阵中包含10")
else:
    print("矩阵中无10")

# 生成器表达式实现高效处理
large_data = (x**2 for x in range(1000000) if x%100 == 0)
```

## 迭代模式进阶

### while循环与计数器模式

while循环适用于不确定迭代次数的场景，常配合计数器或状态标志使用：

```python while_counter.py
# 密码重试机制
max_attempts = 3
attempt = 0

while attempt < max_attempts:
    password = input("请输入密码：")
    if password == "deepseek":
        print("验证成功！")
        break
    attempt += 1
    print(f"剩余尝试次数：{max_attempts - attempt}")
else:
    print("账户已锁定，请联系管理员")

# 计数器优化方案
from itertools import count
print("\n自动计数器：")
for idx in count(1):
    if idx > 5:
        break
    print(f"执行第{idx}次操作")  # 输出1-5
```

#### 使用规范：

1. 始终确保循环条件最终会变为False
2. 复杂计数器建议使用`itertools.count`
3. 资源访问推荐`while`+`try...except`模式
4. 优先考虑`for`循环处理可迭代对象

### 3.2 死循环预防与退出机制

常见安全退出策略实现：

```python safe_loop.py
# 超时退出机制
import time
timeout = 5
start_time = time.time()

print("数据处理监控：")
while True:
    if time.time() - start_time > timeout:
        print("\n处理超时！")
        break
    
    # 模拟数据处理
    print(".", end="", flush=True)
    time.sleep(0.5)

# 最大重试次数限制
max_retries = 3
retries = 0
print("\n\n网络连接重试：")
while retries < max_retries:
    if connect_to_server():  # 假设的连接函数
        print("连接成功")
        break
    retries += 1
    print(f"第{retries}次重试...")
else:
    print("服务器不可达")

# 用户中断处理
print("\n实时数据流处理：")
try:
    while True:
        data = receive_stream_data()
        if process_data(data):
            print("处理完成")
            break
except KeyboardInterrupt:
    print("\n用户主动终止")
```

#### 安全防护策略：

- 强制设置最大迭代上限
- 检查系统时间防止无限阻塞
- 使用回调函数作为退出条件
- 捕捉系统信号实现优雅退出

### 3.3 循环嵌套与复杂度控制

优化深层嵌套循环的方法：

```python loop_nesting.py
# 原始四层嵌套结构
matrix_3d = [[[1,2], [3,4]], [[5,6], [7,8]]]
found = False
for i in range(len(matrix_3d)):
    for j in range(len(matrix_3d[i])):
        for k in range(len(matrix_3d[i][j])):
            if matrix_3d[i][j][k] == 5:
                found = True
                print(f"找到5在[{i}][{j}][{k}]")
                break
        if found: break
    if found: break

# 优化后的扁平化处理
from itertools import product
print("\n优化版三维遍历：")
for i, j, k in product(*[range(2), range(2), range(2)]):
    if matrix_3d[i][j][k] == 5:
        print(f"找到5在[{i}][{j}][{k}]")
        break

# 职责分离优化
def search_value(matrix, target):
    """将搜索逻辑封装为函数"""
    for i, layer in enumerate(matrix):
        for j, row in enumerate(layer):
            for k, val in enumerate(row):
                if val == target:
                    return (i, j, k)
    return None

print("\n函数封装结果：", search_value(matrix_3d, 5))
```

#### 复杂度控制原则：

1. 嵌套层级不超过3层
2. 使用笛卡尔积展开多重循环
3. 合理运用提前返回(return/break)
4. 将内部循环封装为函数

### 3.4 列表解析式语法糖应用

高效数据集处理范式：

```python list_comprehension.py
# 传统循环转换
squares = []
for x in range(10):
    if x % 2 == 0:
        squares.append(x**2)
        
# 等效列表解析式
squares = [x**2 for x in range(10) if x % 2 == 0]

# 多条件嵌套
matrix = [[1,2,3], [4,5,6], [7,8,9]]
flatten = [num for row in matrix 
              for num in row 
              if num > 3]

print("矩阵过滤结果:", flatten)  # [4,5,6,7,8,9]

# 字典推导式应用
users = ['Alice', 'Bob', 'Charlie']
user_map = {name: idx*10 for idx, name in enumerate(users, 1)}
print("用户字典:", user_map)  # {'Alice':10, 'Bob':20, ...}

# 生成器表达式优化内存
big_data = (x**2 for x in range(1000000))
print("\n内存占用比较：")
import sys
print("列表占用：", sys.getsizeof([x**2 for x in range(1000000)]))  # ~8MB
print("生成器占用：", sys.getsizeof((x**2 for x in range(1000000))))  # ~128B
```

#### 解析式选择指南：

| 类型                | 语法              | 内存特征   | 典型场景              |
|---------------------|-------------------|------------|-----------------------|
| 列表解析式          | [...]            | 立即计算   | 中小型数据集处理      |
| 生成器表达式         | (...)            | 惰性计算   | 大数据流处理          |
| 字典解析式           | {k:v for...}     | 立即计算   | 快速构建字典          |
| 集合解析式           | {x for...}       | 立即计算   | 去重操作              |
| 嵌套解析式           | [...]            | 立即计算   | 多维数据筛选          |

### 高级模式示例

```python advanced_generator.py
# 多层嵌套解析式
chessboard = [(x,y) 
    for x in 'ABCDEDGH' 
    for y in range(1,9) 
    if (ord(x)-64+y) % 3 ==0]

# 海象运算符应用
import random
samples = [result for _ in range(10) 
          if (result := random.randint(0,100)) > 50]

# 矩阵转置
matrix = [[1,2], [3,4], [5,6]]
transposed = [[row[i] for row in matrix] 
             for i in range(len(matrix[0]))]
```

关键思想总结：

1. **模式选择**：有限迭代用`for`，条件驱动用`while`
2. **安全迭代**：所有while循环必须具备退出条件
3. **复杂度控制**：使用工具函数分解嵌套结构
4. **语法糖应用**：适度使用解析式保持可读性

## 课后练习：

- 编程实现成绩等级评定系统
- 制作九九乘法表生成器
- 开发质数判断工具
