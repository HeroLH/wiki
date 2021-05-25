----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# cron 库的基本使用 {#index}

[TOC]



 







--------------------------------------------

## 文档版本

|    时间    | /修改人 | 内容     |
| :--------: | :-----: | :------- |
| 2021-05-25 | Herolh  | 文档创建 |
|            |         |          |



## 简介

> go 定时任务实现

[github 地址](https://github.com/robfig/cron)
[go Doc](https://pkg.go.dev/github.com/robfig/cron)



### 巨人的肩膀

[Go 每日一库之 cron](https://mp.weixin.qq.com/s/Ak7RBv1NuS-VBeDNo8_fww)
[Go 每日一库之定时任务库：cron](https://mp.weixin.qq.com/s/swdijAro2k8LuYu7q_La1A)
[Go -- cron 定时任务的用法](https://blog.csdn.net/weixin_30466039/article/details/99940324?utm_medium=distribute.pc_relevant.none-task-blog-baidujs_title-1&spm=1001.2101.3001.4242)



### 安装

```shell
go get github.com/robfig/cron

# 安装指定版本
go get github.com/robfig/cron/v3@v3.0.0
```



## 基本使用

### cron 表达式

#### 规则说明

&emsp;&emsp;cron 表达式是一个好东西，这个东西不仅 Java 的 quartZ 能用到，Go 语言中也可以用到，Linux 也是可以用 `crontab -e` 命令来配置定时任务。Go 语言和 Java 中都是可以精确到秒的，但是 Linux 中不行。cron 表达式代表一个时间的集合，使用 6 个空格分隔的字段表示：

|       字段名       | 是否必须 |    允许的值     | 允许的特定字符 |
| :----------------: | :------: | :-------------: | -------------- |
|    秒 (Seconds)    |    是    |      0-59       | * / , -        |
|    分 (Minute)     |    是    |      0-59       | * / , -        |
|     时 (Hours)     |    是    |      0-23       | * / , -        |
| 日 (Day of month)  |    是    |      1-31       | * / , - ?      |
|     月 (Month)     |    是    | 1-12 或 JAN-DEC | * / , -        |
| 星期 (Day of week) |    否    | 0-6 或 SUM-SAT  | * / , - ?      |

- 月 (Month) 和星期 (Day of week) 字段的值不区分大小写，如：SUN、Sun 和 sun 是一样的。
- 星期 (Day of week) 字段如果没提供，相当于是 *


```shell
 # ┌───────────── min (0 - 59)
 # │ ┌─────────────── hour (0 - 23)
 # │ │ ┌──────────────── day of month (1 - 31)
 # │ │ │ ┌───────────────── month (1 - 12)
 # │ │ │ │ ┌────────────────── day of week (0 - 6) (0 to 6 are Sunday to
 # │ │ │ │ │                   Saturday, or use names; 7 is also Sunday)
 # │ │ │ │ │
 # │ │ │ │ │
 # * * * * *  command to execute
```



#### cron 特定字符说明

##### 星号 `*`

表示 cron 表达式能匹配该字段的所有值。如在第 5 个字段使用星号 (month)，表示每个月



##### 斜线 `/`

表示增长间隔，如第 1 个字段 (minutes) 值是 3-59/15，表示每小时的第 3 分钟开始执行一次，之后每隔 15 分钟执行一次（即 3、18、33、48 这些时间点执行），这里也可以表示为：3/15



##### 逗号 `,`

用于枚举值，如第 6 个字段值是 MON,WED,FRI，表示 星期一、三、五 执行



##### 连字号 `-`

表示一个范围，如第 3 个字段的值为 9-17 表示 9am 到 5pm 直接每个小时（包括 9 和 17）



##### 问号 `?`

只用于 日 (Day of month) 和 星期 (Day of week)，表示不指定值，可以用于代替 *



##### `L、W、#`

Go 中没有 L，W，# 的用法。



#### cron 举例说明

```shell
# 每隔 5 秒执行一次：
*/5 * * * * ?

# 每隔 1 分钟执行一次：
0 */1 * * * ?

# 每天 23 点执行一次：
0 0 23 * * ?

# 每天凌晨 1 点执行一次：
0 0 1 * * ?

# 每月 1 号凌晨 1 点执行一次：
0 0 1 1 * ?

# 在 26 分、29 分、33 分执行一次：
0 26,29,33 * * * ?

# 每天的 0 点、13 点、18 点、21 点都执行一次：
0 0 0,13,18,21 * * ?
```



### 预定义时间规则

为了方便使用，cron 预定义了一些时间规则：

- @yearly：也可以写作 @annually，表示每年第一天的 0 点。等价于 0 0 1 1 *；
- @monthly：表示每月第一天的 0 点。等价于 0 0 1 * *；
- @weekly：表示每周第一天的 0 点，注意第一天为周日，即周六结束，周日开始的那个 0 点。等价于 0 0 * * 0；
- @daily：也可以写作 @midnight，表示每天 0 点。等价于 0 0 * * *；
- @hourly：表示每小时的开始。等价于 0 * * * *。

例如：

```go
func main() {
  c := cron.New()

  c.AddFunc("@hourly", func() {
    fmt.Println("Every hour")
  })

  c.AddFunc("@daily", func() {
    fmt.Println("Every day on midnight")
  })

  c.AddFunc("@weekly", func() {
    fmt.Println("Every week")
  })

  c.Start()

  for {
    time.Sleep(time.Second)
  }
}
```

注意：这样使用一个 `cron.New()` 的定时任务，执行的每个方法是顺序执行的，也就是说并不是同一时刻开始执行。



### 使用 Demo

#### 每秒钟执行一次

```go
package main

import (
    "fmt"
    "time"

    "github.com/robfig/cron/v3"
)

func main() {
    job := cron.New(
        cron.WithSeconds(), // 添加秒级别支持，默认支持最小粒度为分钟
    )
    // 每秒钟执行一次
    job.AddFunc("* * * * * *", func() {
        fmt.Printf("secondly: %v\n", time.Now())
    })
    job.Run()   // 启动
}
```

cron 默认支持到分钟级别，如果需要支持到秒级别，在初始化 cron 时，记得 `cron.WithSeconds()` 参数。





#### 每小时执行一次

```go
// 每小时执行一次
job.AddFunc("0 0 * * * *", func() {
    fmt.Printf("hourly: %v\n", time.Now())
})
// 另一种写法
job.AddFunc("@hourly", func() {
    fmt.Printf("hourly: %v\n", time.Now())
})
```

cron 提供的解析器，可以识别 `@hourly` 这种写法，类似的还有 `daily`，`weekly`，`monthly`，`yearly`，`annually`。





#### 固定时间间隔执行一次

##### @every 写法

```go
// 固定时间间隔执行
job.AddFunc("@every 60s", func() {
    fmt.Printf("every: %v\n", time.Now())
})
```

`@every` 也是解析器提供的功能，`60s` 这个写法，其实就是一个时间区间，类似的还有 `1h`，`1h30m` 等，具体的格式可以通过 [time.ParseDuration](https://golang.org/pkg/time/#ParseDuration) 获取。



##### Schedule 写法

```go
job.Schedule(cron.ConstantDelaySchedule{Delay: time.Minute}, cron.FuncJob(func() {
    fmt.Printf("every: %v\n", time.Now())
}))
```

注意：虽然 `@every` 和 `Schedule` 也能够实现每小时执行一次的这种任务，但是它和 `@hourly `这种方式还是不同的，区别在于：`@hourly` 是在每个小时的开始的时候执行任务，换句话说，如果你在 11:55 分的时候启动了定时任务，那最近一次的执行时间是 12:00。但是 `@every` 和 `Schedule` 这种写法，下次的执行时间会是 12:55，也就是一小时后。





## 源码分析

> [Go cron 定时任务的用法](https://www.cnblogs.com/zuxingyu/p/6023919.html)

### 实现思路

1. 起一个进程，使它一直在后台运行
2. 设置固定的时间间隔或指定一个时间点
3. 到达时间点则执行封装好的函数，实现定时器功能





### 文件目录讲解

```shell
constantdelay.go      #一个最简单的秒级别定时系统。与cron无关
constantdelay_test.go #测试
cron.go               #Cron系统。管理一系列的cron定时任务（Schedule Job）
cron_test.go          #测试
doc.go                #说明文档
LICENSE               #授权书
parser.go             #解析器，解析cron格式字符串城一个具体的定时器（Schedule）
parser_test.go        #测试
README.md             #README
spec.go               #单个定时器（Schedule）结构体。如何计算自己的下一次触发时间
spec_test.go          #测试
```



cron 包主要包含了哪些组件：

1. 解析器：解析 cron 表达式
2. 调度器：计算 Job 下一次执行时间
3. 装饰器：决定 Job 执行模式
4. Job 任务：我们期望定时执行的 func



