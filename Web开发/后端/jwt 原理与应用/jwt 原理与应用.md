> *Made By Herolh*

----------------------------------------------

# 目录 {#index}

[TOC]











--------------------------------------------

# 初识 jwt

## jwt 的基本介绍

### 传统 token 认证

用户登录后，服务端给返回 token, 并将 token 保存在服务端，以后用户再来访问时，需要携带 token， 服务端获取 token 后，再去数据库中获取 token 进行校验



### 什么是 jwt

[jwt 官网](https://jwt.io/)

> json web token， 一般用于用户认证(前后端分离/微信小程序/app 开发)

用户登录后，服务端给返回 token, 但服务端不保存 token，以后用户再来访问时，需要携带 token， 服务端获取 token 后，再做 token 的校验

优势：

相较于传统的 token 。无需在服务端保存 token



## jwt 实现过程

<img src=".assets/image-20200709224207276.png" alt="image-20200709224207276" style="zoom:50%;" />

### 生成 token

- 用户提交用户名和密码给服务端， 如果登录成功，使用 jwt 创建一个 token，并给用户返回:

    ```shell
    eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
    ```

    > **注意：**
    > jwt 生成的token 是由三段字符串组成的， 并用 `.` 连接起来



### token 内容分析

- 第一段字符串，`HEADER` , 内部包含 算法、token类型

    ```python
    {
      "alg": "HS256",		
      "typ": "JWT"
    }
    ```

    > json 转化成字符串，然后做 `base64url` 加密，可反解。本质是base64加密 + url化替换

- 第二段字符串，`PAYLOAD`, 自定义值

    ```python
    {
      "sub": "1234567890",
      "name": "John Doe",
      "exp": 1516239022				# 超时时间
    }
    ```

    > json 转化成字符串，然后做 `base64url` 加密，可反解。本质是base64加密 + url化替换

- 第三段字符串，`VERIFY SIGNATURE`,: 

    - 第一步： 将 第一段和第二段的密文用 `.` 拼接起来

        ```python
        base64UrlEncode(header) + "." +base64UrlEncode(payload)
        ```

        ```python
        eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ
        ```

    - 第二步： 对千两部门的密文进行 H256 加密 + 加盐

        ```python
        HMACSHA256(
          base64UrlEncode(header) + "." + base64UrlEncode(payload),
          your-256-bit-secret
        )
        ```

        第三步：对 H256 加密后的密文再做 base64url 加密

        ```
        base64UrlEncode(
            HMACSHA256(
              base64UrlEncode(header) + "." + base64UrlEncode(payload),
              your-256-bit-secret
            )
        )
        ```



### token 的校验

以后用户再来访问的时候，需要携带 token，后端需要对 token 进行校验

- 第一步：对 token 进行切割

- 第二步：对 第二段进行 base64url 解密， 并获取 `PAYLOAD` 信息，检测 token 是否已经超时

- 第三步：把1,2 段拼接起来再次执行 sha256 加密

    ```python
    将 1,2 部分的密文用 `.` 拼接起来
    对前两部分的密文进行 HSA256 加密 + 加盐
    密文 = base64url(密文)
    如果密文相等，说明 token 未被修改过，认证通过
    ```

    



# {XXX} 进阶

> 中高级的应用



# {XXX} 源码分析





# {XXX} 注意事项





# {XXX} 思考

