> *Made By Herolh*

----------------------------------------------

# 目录 {#index}

[TOC]











--------------------------------------------

# 初识 FastAPI

## FastAPI 的基本介绍

**文档**： [https://fastapi.tiangolo.com](https://fastapi.tiangolo.com/)

**源码**： https://github.com/tiangolo/fastapi 该项目遵循 MIT 许可协议。



### 什么是 FastAPI

> FastAPI 是一个现代，快速( 高性能 )的Web框架，用于基于标准 Python 类型提示使用 Python 3.6+构建 API。

主要功能是：

- **快速**：非常高的性能，看齐的 `NodeJS`和 `GO`(感谢Starlette和Pydantic)。[最快的Python框架之一](https://fastapi.tiangolo.com/#performance)。
- **快速编码**：将功能开发速度提高约200％至300％。
- **错误少**：减少约40％的人为错误。
- **直观**：强大的编辑器支持。完成无处不在。调试时间更少。
- **简易**：旨在易于使用和学习。减少阅读文档的时间。
- **短**：最小化代码重复。每个参数声明中的多个功能。更少的错误。
- **健壮**：获取可用于生产的代码。具有自动交互式文档。
- **基于标准**：基于（并完全兼容）API的开放标准：[OpenAPI](https://github.com/OAI/OpenAPI-Specification)( 以前称为Swagger ) 和 [JSON Schema](http://json-schema.org/)。
- 

### FastAPI 的安装

```shell
pip install fastapi
```

你还会需要一个 ASGI 服务器，生产环境可以使用 [Uvicorn](http://www.uvicorn.org/) 或者 [Hypercorn](https://gitlab.com/pgjones/hypercorn)。

```shell
pip install uvicorn
```



### 可选依赖

#### 用于 Pydantic：

- [`ujson`](https://github.com/esnme/ultrajson) - 更快的 JSON 「解析」。
- [`email_validator`](https://github.com/JoshData/python-email-validator) - 用于 email 校验。

#### 用于 Starlette：

- [`requests`](http://docs.python-requests.org/) - 使用 `TestClient` 时安装。
- [`aiofiles`](https://github.com/Tinche/aiofiles) - 使用 `FileResponse` 或 `StaticFiles` 时安装。
- [`jinja2`](http://jinja.pocoo.org/) - 使用默认模板配置时安装。
- [`python-multipart`](https://andrew-d.github.io/python-multipart/) - 需要通过 `request.form()` 对表单进行「解析」时安装。
- [`itsdangerous`](https://pythonhosted.org/itsdangerous/) - 需要 `SessionMiddleware` 支持时安装。
- [`pyyaml`](https://pyyaml.org/wiki/PyYAMLDocumentation) - 使用 Starlette 提供的 `SchemaGenerator` 时安装（有 FastAPI 你可能并不需要它）。
- [`graphene`](https://graphene-python.org/) - 需要 `GraphQLApp` 支持时安装。
- [`ujson`](https://github.com/esnme/ultrajson) - 使用 `UJSONResponse` 时安装。

#### 用于 FastAPI / Starlette：

- [`uvicorn`](http://www.uvicorn.org/) - 用于加载和运行你的应用程序的服务器。
- [`orjson`](https://github.com/ijl/orjson) - 使用 `ORJSONResponse` 时安装。

你可以通过以下 命令来安装以上所有依赖。

```shell
pip install fastapi[all]
```





### Hello World

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# 以下相当于命令行中的 uvicorn main:app --reload
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=3000)
```

使用浏览器访问 [http://127.0.0.1:3000](http://127.0.0.1:3000)，你将会看到如下 JSON 响应：

```python
{"Hello":"World"}
```

 

#### 命令行启动

`uvicorn main:app` 命令含义如下:

- `main`：`main.py` 文件（一个 Python「模块」）。
- `app`：在 `main.py` 文件中通过 `app = FastAPI()` 创建的对象。
- `--reload`：让服务器在更新代码后重新启动。仅在开发时使用该选项。



# FastAPI 的初步使用

## FastAPI 基础语法

###  路由系统

#### 路径参数

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, arg: str = None):
    return {"item_id": item_id, "arg": arg}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=3000)
```

路径参数 `item_id` 的值将作为参数 `item_id` 传递给你的函数。所以，如果你运行示例并访问 http://127.0.0.1:8000/items/5?arg=1，将会看到如下响应：

```
{"item_id":5,"arg":"1"}
```





### FastAPI 模拟场景





# FastAPI 进阶

> 中高级的应用



# FastAPI 源码分析





# FastAPI 注意事项





# FastAPI 思考

