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