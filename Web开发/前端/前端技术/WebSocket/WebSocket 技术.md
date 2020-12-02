> *Made By Herolh*

----------------------------------------------

# 目录 {#index}

[TOC]











--------------------------------------------

# 初识 WebSocket

[博客园 - 武沛奇 - 你真的了解 WebSocket 吗](https://www.cnblogs.com/wupeiqi/p/6558766.html)

## WebSocket 的基本介绍

### 什么是 WebSocket

> &emsp;&emsp;WebSocket 协议是基于 TCP 的一种新的协议。WebSocket 最初在HTML5 规范中被引用为 TCP 连接，作为基于 TCP 的套接字 API 的占位符。它实现了浏览器与服务器全双工( full-duplex )通信。其本质是保持 TCP 连接，在浏览器和服务端通过 Socket 进行通信。

```shell
http 是一个网络协议( 无状态短链接 )
https 是一个网络协议( 无状态短链接 )
websocket  是一个网络协议( 让浏览器和服务端创建链接支持，默认不再断开， 两端就可以完成互相之间的收发数据 )
```





# WebSocket 的实现原理

- **握手环节**
    - 浏览器生成一个随机字符串，并将随即字符串发送给服务端
    - 服务端收到随机字符串后，让它和全球公认的魔法字符串进行拼接，在进行 sha1 加密，再进行 base64 加密
    - 将密文返回给拥护浏览器
    - 拥护浏览器自动化进行校验



- **收发数据，密文**

    ```shell
    数据解密时需要读取数据第 2 个字节的后 7 位，如果
    
    127
    
    126
    
    <= 125
    ```

    

## 握手环节

> 验证服务端是否支持 websocket 协议



### 浏览器生成随机字符串发送给服务端

#### 启动服务端

&emsp;&emsp;启动 Socket 服务器后，等待用户【连接】，然后进行收发数据。

```python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('127.0.0.1', 8002))
sock.listen(5)
# 等待用户连接
conn, address = sock.accept()
# 获取客户端的【握手】信息
data = conn.recv(1024)
print(data.decode())
```



#### 客户端链接

&emsp;&emsp;当客户端向服务端发送连接请求时，不仅连接还会发送【握手】信息，并等待服务端响应，至此连接才创建成功！

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

</body>
    <script type="text/javascript">
        var socket = new WebSocket("ws://127.0.0.1:8002/xxoo");
        // ...
    </script>
</html>
```



#### 服务端接收到客户端的请求头

```shell
GET /xxoo HTTP/1.1
Host: 127.0.0.1:8002
Connection: Upgrade
Pragma: no-cache
Cache-Control: no-cache
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36
Upgrade: websocket
Origin: file://
Sec-WebSocket-Version: 13
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cookie: lang=zh-CN
Sec-WebSocket-Key: 6ZCfv6CkFfxlP1ALZM7koQ==
Sec-WebSocket-Extensions: permessage-deflate; client_max_window_bits
```

> 客户端生成的随机字符串：`Sec-WebSocket-Key: 6ZCfv6CkFfxlP1ALZM7koQ==`



### 建立连接【握手】
请求和响应的【握手】信息需要遵循规则：
- 从请求【握手】信息中提取 `Sec-WebSocket-Key`
- 利用 `magic_string` 和 `Sec-WebSocket-Key` 进行 `hmac1` 加密，再进行 `base64` 加密
- 将加密结果响应给客户端
> *注：magic string为：258EAFA5-E914-47DA-95CA-C5AB0DC85B11*



#### 启动服务器

```python
import socket
import base64
import hashlib


def get_headers(data):
    """
    将请求头格式化成字典
    :param data:
    :return:
    """
    header_dict = {}
    data = str(data, encoding='utf-8')

    for i in data.split('\r\n'):
        print(i)
    header, body = data.split('\r\n\r\n', 1)
    header_list = header.split('\r\n')
    for i in range(0, len(header_list)):
        if i == 0:
            if len(header_list[i].split(' ')) == 3:
                header_dict['method'], header_dict['url'], header_dict['protocol'] = header_list[i].split(' ')
        else:
            k, v = header_list[i].split(':', 1)
            header_dict[k] = v.strip()
    return header_dict


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('127.0.0.1', 8002))
sock.listen(5)

conn, address = sock.accept()
data = conn.recv(1024)
headers = get_headers(data)  # 提取请求头信息
# 对请求头中的sec-websocket-key进行加密
response_tpl = "HTTP/1.1 101 Switching Protocols\r\n" \
               "Upgrade:websocket\r\n" \
               "Connection: Upgrade\r\n" \
               "Sec-WebSocket-Accept: %s\r\n" \
               "WebSocket-Location: ws://%s%s\r\n\r\n"
magic_string = '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'
value = headers['Sec-WebSocket-Key'] + magic_string
ac = base64.b64encode(hashlib.sha1(value.encode('utf-8')).digest())
response_str = response_tpl % (ac.decode('utf-8'), headers['Host'], headers['url'])
# 响应【握手】信息
conn.send(bytes(response_str, encoding='utf-8'))
```





## 收发数据