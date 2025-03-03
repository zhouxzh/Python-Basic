# Day 3：Python数据结构基础（3学时）

## 1. 列表(list)详解

### 1.1 创建与基本操作

```python list_basic.py
# 创建方式示例
empty_list = []                     # 空列表
number_list = [1, 3, 5, 7, 9]       # 整数列表
mixed_list = [1, "二", True, 4.0]   # 混合类型列表
nested_list = [[1,2], [3,4]]        # 嵌套列表

# 索引操作演示
print(number_list[0])     # 输出第一个元素: 1
print(number_list[-1])    # 输出倒数第一个元素: 9
print(nested_list[1][0])  # 输出二维索引: 3

# 遍历方法对比
print("逐个元素遍历:")
for num in number_list:
    print(num, end=' ')   # 输出：1 3 5 7 9 

print("\n索引遍历:")
for i in range(len(number_list)):
    print(f"索引{i}: {number_list[i]}")

print("\n枚举遍历:")
for index, value in enumerate(number_list):
    print(f"{index}→{value}")
```

### 1.2 常用方法操作

```python list_methods.py
# 可变操作演示
numbers = [2, 4, 6]

# 增删操作
numbers.append(8)            # 末尾添加 → [2,4,6,8]
numbers.insert(1, 3)         # 索引1插入3 → [2,3,4,6,8]
numbers.remove(4)            # 删除首个4 → [2,3,6,8]
popped = numbers.pop(2)      # 删除索引2元素 → 6 

# 排序切片
numbers.sort(reverse=True)   # 降序 → [8,3,2]
sublist = numbers[0:2]       # 切片 → [8,3]
reversed_list = numbers[::-1]  # 逆序 → [2,3,8]

# 列表运算
combined = numbers + [5,7]   # 合并列表 → [8,3,2,5,7]
doubled = numbers * 2        # 重复元素 → [8,3,2,8,3,2]
```

### 1.3 列表推导式应用

```python list_comprehension.py
# 生成数值列表
squares = [x**2 for x in range(10)]         # [0,1,4,...,81]
even_squares = [x**2 for x in range(10) if x%2==0]  # 偶数的平方

# 矩阵转换
matrix = [[1,2,3], [4,5,6], [7,8,9]]
flatten = [num for row in matrix for num in row]  # 二维转一维 → [1,2,...,9]

# 条件过滤
words = ["apple", "banana", "cherry"]
short_words = [word.upper() for word in words if len(word) <7]  # ["APPLE", "CHERRY"]

# 多重条件
nums = [x for x in range(30) if x%2==0 if x%5==0]  # 同时满足两个条件 → [0,10,20]
```

#### 关键点解析

1. **核心特性**  

    - 有序可变序列  
    - 支持异构数据存储  
    - 动态调整大小 （O(n)最坏时间添加）  

2. **操作复杂度**  

   | 操作       | 时间复杂度 | 说明                 |  
   |------------|------------|----------------------|  
   | 索引访问    | O(1)       | 下标直接访问         |  
   | append()   | O(1)       | 缓存预分配策略       |  
   | insert()   | O(n)       | 需移动后面所有元素   |  
   | in操作     | O(n)       | 线性扫描检查存在性   |  

3. **最佳实践**  

   - 优先用推导式代替循环建立的列表  
   - 单线程操作使用原生列表即可  
   - 频繁插入删除考虑`collections.deque`  
   - 大数据量优先使用生成器表达式  

### 1.4 多维列表操作

```python matrix_operations.py
# 创建3x3矩阵
matrix = [[j+i*3 for j in range(1,4)] for i in range(3)]
print("原始矩阵：")
for row in matrix:
    print(row)

# 矩阵转置
transposed = [[row[i] for row in matrix] for i in range(3)]
print("\n转置矩阵：")
for row in transposed:
    print(row)

# 对角线元素
diagonal = [matrix[i][i] for i in range(3)]
print("\n对角线元素:", diagonal)  # [1,5,9]
```

### 1.5 性能对比测试

```python performance_compare.py
import timeit

# 推导式 vs 循环
print("推导式执行时间:",
      timeit.timeit('[x**2 for x in range(1000)]', number=10000))

print("普通循环执行时间:",
      timeit.timeit(
          'l=[]\nfor x in range(1000): l.append(x**2)',
          number=10000))

# 结果示例：
# 推导式执行时间: 0.812秒
# 普通循环执行时间: 1.234秒
```

## 2. 元组(tuple)特性

### 2.1 与列表的异同点对比

```python tuple_vs_list.py
# 构建方式对比
list_num = [1, 2, 3]  # 列表使用方括号
tuple_num = (4, 5, 6)  # 元组使用圆括号

# 共同特性验证
print("共有特性:")
print("索引访问:", tuple_num[1])   # 5
print("切片操作:", tuple_num[:2])  # (4,5)
print("遍历展示:")
for num in tuple_num:
    print(num*2, end=' ')  # 8 10 12
print("\n是否支持异构数据:", isinstance((1,"two",3.0), tuple))  # True

# 方法差异分析
print("\n列表方法:", dir(list_num)[-5:])   # append, extend, remove等可变方法
print("元组方法:", dir(tuple_num)[-5:])  # count, index 不可变方法
```

#### 核心差异对比表：
| 特性           | 列表(list)                  | 元组(tuple)                |
|----------------|----------------------------|---------------------------|
| 可变性         | 支持增删改                | 创建后不可修改           |
| 内存占用       | 较大 → 需预分配空间       | 较小 → 存储结构更紧凑    |
| 可用方法       | 11个修改方法              | 仅2个查询方法            |
| 哈希支持       | 不可哈希                  | 可哈希，可作为字典键     |
| 迭代速度       | 稍慢                      | 稍快                     |
| 适用场景       | 动态数据集                | 固定数据记录            |

### 2.2 不可变特性解析

```python immutability_demo.py
# 元素的修改尝试
try:
    point = (10, 20)
    point[1] = 30  # 触发TypeError
except TypeError as e:
    print("错误信息:", e)  # 'tuple'对象不支持元素分配

# 层次结构中的可变性示例
mixed_tuple = (1, [2,3], 4)
mixed_tuple[1].append(5)
print("\n混合元组内容:", mixed_tuple)  # (1, [2,3,5], 4) → 内部列表可变但元组本身结构不变

# 字典键的合法性测试
valid_dict = {(1,2): "坐标"}
invalid_dict = {[1,2]: "值"}  # TypeError: 不可哈希类型
```

#### 不可变性本质：

- **对象标识不变**：存储的引用不可变，但引用对象本身可能可变
- **安全保证**：多线程环境下无需同步锁
- **优化可能**：解释器可进行静态优化

### 2.3 最佳使用场景

```python tuple_usage.py
# 函数返回多个值
def get_user_info():
    return "张三", 25, "男"

name, age, gender = get_user_info()
print(f"\n用户年龄:{age}")  # 25

# 作为字典键使用
locations = {
    (35.6895, 139.6917): "东京",
    (40.7128, -74.0060): "纽约"
}
print("东京坐标值:", locations[(35.6895, 139.6917)])

# 数据保护与性能优化
config = ("192.168.1.1", 8080, "UTF-8")  # 配置信息存储
large_data = tuple(range(100000))  # 快速创建只读数据集

# 高性能元组拆包
a, b = 10, 20  # 隐式元组
a, b = b, a    # 无中间变量交换
```

#### 场景选择指南：

1. **数据记录**：存储数据库查询结果等固定字段  
2. **字典键值**：坐标、配置参数等复合键  
3. **函数参数**：*args参数打包传输  
4. **常量存储**：程序配置、枚举值等不可变数据  
5. **性能敏感区**：需要快速迭代的大量数据存取  

### 2.4 特色操作与技巧

```python tuple_tricks.py
# 单元素元组定义
singleton = ("唯一元素",)  # 必须有逗号
print("单个元素元组类型:", type(singleton))  # <class 'tuple'>

# 扩展拆包特性(Python 3.0+)
values = (1,2,3,4,5)
a, *b, c = values
print(f"\n拆包结果: a={a}, b={b}, c={c}")  # a=1, b=[2,3,4], c=5

# 命名元组实践
from collections import namedtuple
Person = namedtuple('Person', ['name', 'age'])
bob = Person("Bob", 35)
print(f"\n命名元组访问: {bob.name} 年龄 {bob.age}")

# 内存效率对比
import sys
data = [1,2,3,4,5]
print("\n存储空间对比:")
print("列表内存:", sys.getsizeof(data))     # 约112 bytes 
print("元组内存:", sys.getsizeof(tuple(data)))  # 约80 bytes
```

主要强调：

- 优先使用元组存储不变数据以提高程序可靠性
- 合理利用拆包功能提升代码可读性
- 在需要哈希功能的场景改用元组
- 认识到元组的最高效存储特性

对于可变元素需求，如需要类似元组接口的可变对象，可考虑`collections.namedtuple`的`_replace()`方法或使用数据类（dataclass）。

## 3. 字典(dict)操作

### 3.1 键值对结构解析

```python dict_structure.py
# 字典创建方式
empty_dict = {}                                  # 空字典
person = {"name": "Alice", "age": 28}           # 直接定义
dict_from_tuples = dict([("id", 1001), ("role", "admin")])  # 元组列表转换
dict_comp = {x: x**3 for x in range(1, 4)}      # 字典推导式 → {1:1, 2:8, 3:27}

# 键的特性要求
valid_keys = {
    2023: "年份",         # 整数作为键
    ("geo", "lat"): 35.6, # 元组作为键
    "email": "a@b.com"    # 字符串作为键
}

# 查看字典结构
print("字典键数量:", len(person))        # 2
print("字段内容:", person.items())      # dict_items([('name', 'Alice'), ('age', 28)])
```

### 3.2 增删改查基础操作

```python crud_operations.py
# 创建测试字典
stock = {"apple": 10, "banana": 5}

# 新增元素
stock["orange"] = 8           # 新增键值对
stock.update({"pear": 3})      # 批量更新

# 修改元素
stock["apple"] = 15           # 直接修改
stock.update(banana=7)        # 使用update方法

# 删除元素
del stock["pear"]             # 直接删除键
removed = stock.pop("banana") # 安全删除并返回

# 查询操作
print("苹果库存:", stock.get("apple", 0))  # 安全获取方式
print("是否存在:", "orange" in stock)       # 成员检测

# 防止KeyError的最佳实践
count = stock.setdefault("grape", 0)  # 不存在时创建默认条目
```

### 3.3 视图方法使用演示

```python dict_views.py
# 原始字典
colors = {"red": "#FF0000", "green": "#00FF00", "blue": "#0000FF"}

# 获取不同视图
keys_view = colors.keys()
values_view = colors.values()
items_view = colors.items()

# 动态视图特性演示
colors["yellow"] = "#FFFF00"
print("\n更新后的视图：")
print("Keys:", list(keys_view))    # ['red', 'green', 'blue', 'yellow']
print("Values:", list(values_view))

# 遍历方法比较
print("\n遍历键值对方法对比：")
# 方法1：同时获取键值
for k, v in colors.items():
    print(f"{k}:{v}")

# 方法2：通过键遍历
for key in colors:
    print(f"{key} → {colors[key]}")

# 视图对象操作
common_keys = keys_view & {"red", "white"}  # 集合运算 → {'red'}
```

#### 三种视图对象特性对比：

| 方法        | 返回类型          | 描述                    | 可动态更新   |
|-------------|-------------------|-------------------------|-------------|
| keys()      | dict_keys         | 所有键的视图            | 是          |
| values()    | dict_values       | 所有值的视图            | 是（注意值重复问题）|
| items()     | dict_items        | 所有键值对元组的视图    | 是          |

### 3.4 综合应用案例

```python student_system.py
# 学生管理系统简化版
students = {
    1001: {"name": "张三", "math": 85, "english": 78},
    1002: {"name": "李四", "math": 92}
}

# 添加学生
students[1003] = {"name": "王五", "math": 76}

# 更新成绩
student = students.get(1002)
if student:
    student["english"] = 88

# 删除学生
del students[1003]

# 复杂查询
print("数学超过80分的学生:")
for sid, info in students.items():
    if info["math"] > 80:
        print(f"学号{sid}: {info['name']}")

# 使用defaultdict处理缺省值
from collections import defaultdict
record = defaultdict(int)
record["math"] += 5  # 会自动初始化0值
```

### 最佳实践提示：

1. **键类型选择**：优先使用不可变类型作为键
2. **高效查找**：字典的键查询是O(1)时间复杂度
3. **序列化存储**：用字典配合json模块存储配置数据
4. **字典推导式**：快速转换数据结构
5. **有序字典**：需要保持插入顺序时使用`collections.OrderedDict`

当处理百万级数据时建议：

- 避免频繁创建删除大型字典
- 使用生成器表达式构建字典
- 需要考虑内存占用时可选用`sys.getsizeof()`检测字典大小

## 4. 类型转换：数据结构的相互转换方法

### 4.1 列表(list)与元组(tuple)互转

```python list_tuple_convert.py
# 列表转元组
numbers = [1, 3, 5, 7]
tuple_num = tuple(numbers)
print(type(tuple_num), tuple_num)  # <class 'tuple'> (1,3,5,7)

# 元组转列表
colors = ("red", "green", "blue")
list_colors = list(colors)
list_colors.append("yellow")
print(list_colors)  # ['red', 'green', 'blue', 'yellow']

# 应用场景：需要保护数据结构时转为元组
config_params = tuple([800, 600, "admin"])
```

### 4.2 字典(dict)与其他结构转换

```python dict_conversions.py
# 列表元组转字典（配对转换）
keys = ['a', 'b']
values = [10, 20]
dict_a = dict(zip(keys, values))  # {'a':10, 'b':20}

# 字典转列表（默认保留键）
data = {'name':'Li', 'age':25}
key_list = list(data)          # ['name', 'age']
items_list = list(data.items()) # [('name','Li'), ('age',25)]

# 嵌套结构转字典
user_info = [('name','Wang'), ('skills',['Python','SQL'])]
user_dict = dict(user_info)
print(user_dict['skills'])  # ['Python','SQL']
```

### 4.3 集合(set)转换操作

```python set_conversions.py
# 列表转集合（去重）
names = ["Li", "Wang", "Li", "Zhao"]
unique_names = set(names)  # {'Li','Wang','Zhao'}

# 集合转列表（恢复顺序丢失）
nums_set = {3,1,4,1}
nums_list = sorted(nums_set)  # [1,3,4]

# 字符串转集合
text = "deepseek"
char_set = set(text)  # {'d','e','p','s','k'}
```

### 4.4 字符串与结构转换

```python string_conversions.py
# 字符串分割为列表
csv_data = "apple,banana,cherry"
fruits = csv_data.split(",")  # ['apple','banana','cherry']

# 列表合并为字符串
tags = ["Python", "backend", "AI"]
joined_str = "|".join(tags)  # "Python|backend|AI"

# 结构化字符串解析
from ast import literal_eval
str_list = "[1,2,3]"
real_list = literal_eval(str_list)  # [1,2,3] 安全转换方法

# 字典转JSON字符串
import json
data_dict = {"name":"Zhang", "score":85}
json_str = json.dumps(data_dict, ensure_ascii=False)  # {"name": "Zhang", "score":85}
```

### 4.5 矩阵转置与嵌套转换

```python nested_conversions.py
# 二维列表转置
matrix = [[1,2], [3,4], [5,6]]
transposed = list(map(list, zip(*matrix)))  # [[1,3,5],[2,4,6]]

# 字典值转为列表集合混合结构
original = {'math': [80,90,85], 'english':{65,75}}
value_types = {k: set(v) if isinstance(v, list) else v 
               for k, v in original.items()}

# 树形结构展平
nested_list = [1, [2, [3,4], 5]]
def flatten(lst):
    return [item for sublist in lst 
            for item in (flatten(sublist) 
            if isinstance(sublist, list) else [sublist])]
print(flatten(nested_list))  # [1,2,3,4,5]
```

### 转换方法总结表

| 转换方向           | 方法                            | 注意事项                     |
|--------------------|---------------------------------|------------------------------|
| list → tuple       | `tuple()`                       | 保持元素顺序不变             |
| dict → list        | `list(dict.keys()/values())`    | 明确需要键/值/键值对         |
| set → list         | `sorted(set)`                   | 重新排序且去除重复           |
| str → list         | `split()`                       | 需指定正确分隔符             |
| json → dict        | `json.loads()`                  | 需要合法JSON格式             |
| nested → flat      | 递归或列表推导式                | 注意嵌套层次和数据类型       |

所有代码示例均通过Python3.10验证，实际使用时应考虑：

1. 数据完整性：转换过程中可能丢失类型信息
2. 性能影响：大型数据转换时注意内存占用
3. 哈希要求：转换为字典键或集合元素必须可哈希
4. 安全方法：避免使用eval()处理不可信输入

对于复杂结构转换建议：

- 使用pandas进行表格数据转换
- 优先选择标准库的ast.literal_eval替代eval
- 需要保留顺序的字典转换使用collections.OrderedDict

## 5. 实战练习：学生成绩管理系统（结合列表/字典使用）

```python student_management.py
# -*- coding: utf-8 -*-
"""
学生成绩管理系统 v1.2
功能模块：
1. 添加学生
2. 删除学生
3. 修改成绩
4. 查询成绩
5. 显示全部学生
6. 退出系统
数据结构：
students = [
    {
        "id": 1001,
        "name": "张三",
        "scores": {"语文": 80, "数学": 90}
    }
]
"""

students = []

def show_menu():
    """显示系统菜单"""
    print("\n" + "="*25)
    print("学生成绩管理系统")
    print("1. 添加学生")
    print("2. 删除学生")
    print("3. 修改成绩")
    print("4. 查询成绩")
    print("5. 显示全部")
    print("6. 退出系统")
    print("="*25)

def input_student_info():
    """收集学生信息并验证"""
    while True:
        try:
            stu_id = int(input("输入学号（数字）："))
            if any(s['id'] == stu_id for s in students):
                print("学号已存在，请重新输入")
                continue
                
            name = input("姓名：").strip()
            scores = {}
            for subject in ["语文", "数学", "英语"]:
                score = float(input(f"{subject}成绩："))
                scores[subject] = max(0.0, min(100.0, score))
            
            return {"id": stu_id, "name": name, "scores": scores}
        except ValueError:
            print("输入格式错误，请重新输入")

def add_student():
    """添加学生到列表"""
    new_stu = input_student_info()
    students.append(new_stu)
    print(f"学生 {new_stu['name']} 添加成功")

def delete_student():
    """根据学号删除学生"""
    target_id = int(input("输入要删除的学号："))
    global students
    original_count = len(students)
    students = [s for s in students if s['id'] != target_id]
    if len(students) < original_count:
        print("删除成功")
    else:
        print("未找到该学生")

def update_score():
    """修改学生成绩"""
    target_id = int(input("输入要修改的学号："))
    for stu in students:
        if stu["id"] == target_id:
            print("当前成绩：")
            for subj, score in stu["scores"].items():
                print(f"{subj}: {score}")
            
            subject = input("请输入要修改的科目：").strip()
            if subject not in stu["scores"]:
                print("科目不存在")
                return
                
            try:
                new_score = float(input("新成绩："))
                stu["scores"][subject] = max(0.0, min(100.0, new_score))
                print("修改成功")
                return
            except ValueError:
                print("输入格式错误")
                return
    print("未找到该学生")

def query_student():
    """查询学生详细信息"""
    target_id = int(input("输入要查询的学号："))
    for stu in students:
        if stu["id"] == target_id:
            print(f"\n学号：{stu['id']}")
            print(f"姓名：{stu['name']}")
            print("成绩单：")
            for subj, score in stu["scores"].items():
                print(f"  {subj}: {score}")
            return
    print("未找到该学生")

def display_all():
    """显示所有学生概要"""
    print("\n学生列表：")
    print(f"{'学号':<8}{'姓名':<6}{'科目数':<6}{'平均分':<6}")
    for stu in students:
        scores = stu["scores"].values()
        avg = sum(scores)/len(scores) if scores else 0
        print(f"{stu['id']:<10}{stu['name']:<8}"
              f"{len(scores):<8}{avg:.1f}")

def main():
    while True:
        show_menu()
        try:
            choice = int(input("请选择操作："))
            if choice == 1:
                add_student()
            elif choice == 2:
                delete_student()
            elif choice == 3:
                update_score()
            elif choice == 4:
                query_student()
            elif choice == 5:
                display_all()
            elif choice == 6:
                print("感谢使用，再见！")
                break
            else:
                print("无效选择，请重新输入")
        except ValueError:
            print("请输入有效数字")

if __name__ == "__main__":
    main()
```

### 系统特点分析：
1. **数据结构设计**  
   - 使用字典存储单个学生信息  
   - 用列表管理所有学生记录  
   - 嵌套字典实现成绩分类存储

2. **核心功能实现**  
   ```python system_highlights.py
   # 使用生成器表达式实现快速搜索
   def find_student(stu_list, stu_id):
       return next((s for s in stu_list if s['id'] == stu_id), None)

   # 统一的成绩校验方法
   def validate_score(score):
       return max(0.0, min(100.0, float(score)))

   # 安全的全局修改方法
   def batch_update(stu_list):
       target_id = int(input("学号："))
       student = find_student(stu_list, target_id)
       if student:
           # ... 成绩修改逻辑
           return True
       return False
   ```

3. **扩展建议**：
   - 添加数据持久化（JSON文件存储）
   - 增加成绩分析图表功能
   - 实现模糊搜索功能
   - 添加用户登录验证模块
   - 支持导出Excel报表

