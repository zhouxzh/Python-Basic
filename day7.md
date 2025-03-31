# Day 7：Python网络编程（3学时）

#### **一、网络编程概述**
1. 网络通信基础  
   - 协议（TCP/UDP/IP/HTTP）  
   - IP地址与端口  
   - 客户端-服务端模型  
2. Python网络编程常用库  
   - `socket`（底层网络通信）  
   - `requests`（HTTP客户端）  
   - `http.server`（简单HTTP服务端）  

---

#### **二、Socket编程基础**
1. **TCP Socket**  
   - 服务端流程：`socket()` → `bind()` → `listen()` → `accept()` → `recv()`/`send()` → `close()`  
   - 客户端流程：`socket()` → `connect()` → `send()`/`recv()` → `close()`  
   - 示例：实现一个简单的回声服务器（Echo Server）  

2. **UDP Socket**  
   - 服务端与客户端的区别（无连接）  
   - 示例：实现UDP消息发送与接收  

3. 代码实践  
   ```python
   # TCP服务端示例
   import socket
   server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   server.bind(('localhost', 8888))
   server.listen()
   client, addr = server.accept()
   data = client.recv(1024)
   client.send(data)
   ```

---

#### **三、应用层协议与HTTP编程**
1. **HTTP协议基础**  
   - 请求与响应格式（GET/POST）  
   - 状态码（200/404/500）  

2. **使用`requests`库**  
   - 发送GET/POST请求  
   - 处理JSON数据与API调用  

3. **使用`http.server`创建简单HTTP服务**  
   ```python
   from http.server import SimpleHTTPRequestHandler, HTTPServer
   server = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
   server.serve_forever()
   ```

---

#### **四、实战项目**
1. **简单聊天室**  
   - 基于TCP的多客户端通信（使用多线程或`select`模块）  
2. **网页爬虫**  
   - 使用`requests`获取网页内容并解析数据  
3. **REST API调用**  
   - 调用公开API（如天气、新闻接口）并处理返回数据  

---

#### **五、常见问题与调试**
1. 常见错误  
   - 连接拒绝（Connection Refused）  
   - 端口占用（Address Already in Use）  
2. 工具辅助  
   - 使用`netstat`/`telnet`检查端口  
   - Wireshark抓包分析（可选）  

---

#### **六、进阶方向**
1. 多线程与异步IO（`asyncio`）  
2. Web框架（Flask/Django的简单网络应用）  
3. WebSocket实时通信  

---

#### **七、参考资料**
1. 官方文档  
   - [Python `socket`库](https://docs.python.org/3/library/socket.html)  
   - [Python `requests`库](https://docs.python-requests.org/)  
2. 书籍推荐  
   - 《Python网络编程攻略》  
   - 《Foundations of Python Network Programming》  

---

这个提纲覆盖了从基础Socket编程到实际应用的核心内容，适合配合代码实践逐步学习。可根据学习者的进度调整深度或扩展项目（如添加安全通信SSL/TLS）。