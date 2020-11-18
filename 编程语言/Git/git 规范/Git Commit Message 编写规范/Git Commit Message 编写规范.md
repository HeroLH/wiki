----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# Git Commit Message 编写规范 {#index}

[TOC]











# Git Commit Message 模板

## 使用注意事项:

- 使用 git 命令提交有问题不知道分行怎么办，参考下先输入第一个引号，按 Enter 即可换行，完成后再补齐后面的引号

    ```shell
    # 步骤一: 输入第一行
    git commit -m "1. 第一行
    
    # 步骤二: 按Enter 输入第二行
    git commit -m "1. 第一行
    2. 第二行 
    
    # 步骤三: 输入完毕，补齐引号，提交！
    git commit -m "1. 第一行
    2. 第二行"
    ```





# Git Commit Message 规范参照

## 目的

- 提供更多的历史信息,方便 `快速浏览` 和 `暂时回滚`

- 可以使用命令 `git log HEAD --pretty=format:%s`  预览此前的提交信息.

- 可以快速过滤某些 commit (比如文档改动) , 以便快速查找信息

- 可以直接从 commit 生成 Change Log (过滤出 feature 和 fix type 的 提交即可)



## 参考案例

-  [如何写好git commit message](https://www.cnblogs.com/deng-cc/p/6322122.html)
-  [阮一峰的网络日志：Commit message 和 Change log 编写指南](http://www.ruanyifeng.com/blog/2016/01/commit_message_change_log.html)
-  [写好 Git Commit 信息的 7 个建议](http://blog.jobbole.com/92713/)
-  [angular](https://github.com/angular/angular)
-  [commit-message-test-project](https://github.com/cpselvis/commit-message-test-project)
-  [babel-plugin-istanbul](https://github.com/istanbuljs/babel-plugin-istanbul)
-  [conventional-changelog](https://github.com/conventional-changelog/conventional-changelog)



## 总体方案

```shell
<type>(<scope>): <subject>
<BLANK LINE (空一行)>
<body>
<BLANK LINE (空一行)>
<footer>
```

每次提交, commit message 都包括三个部分 : 
• Header
• Body
• Footer
其中, `Header` 是必须的, `Body` 和 `Footer` 可以选填.
不管是 哪一个部分, 任何一行都不得查过 72个 字符(或 100个字符 ). 这是为了避免自动换行影响美观。



## 对 Header，Body，Footer的介绍

### Header

Header 部分尽量只有一行, `<type>(<scope>): <subject>`  包括三个字段: `type`(必须) , `scope`(可选) , `subject`(必须)

#### type

> `type` 用于说明 commit 的类别 , 只允许使用下面的七个标识

- **feat**        : 新功能,新特性(feature)
- **fix**           : 修复 Bug
- **docs**       : 仅仅修改了文档，比如 README, CHANGELOG, CONTRIBUTE等等(documentation)  
- **style**       : 仅仅修改了空格、格式缩进、逗号等等，不改变代码逻辑(不影响代码运行的变动)  
- **refactor** : 代码重构，没有加入新功能或者修复bug......
- **perf**        : 优化相关，比如提升性能、体验......
- **test**         : 测试用例，包括单元测试、集成测试......
- **chore**      : 改变构建流程、或者增加依赖库、辅助工具......
- **revert**     : 回滚到上一个版本

如果 `type` 为 `feat` 和 `fix`, 则该 commit 肯定会出现在 Change log 之中. 其他情况可以自行决定是否需要放入 ChangeLog中.



#### scope

> `scope` 用于说明 commit 影响的范围, 比如 数据层, 控制层, 视图层...... , 视项目的不同而不同



#### 1. subject

>  `subject` 是 commit 目的的简短描述 , 不超过50个字符

```shell
# 以动词开头,使用第一人称现在时, 比如 change, 而不是 changed 或者 changes
# 第一个字母小写
# 结尾不加句号
```



### Body
> Body 部分是对本次 commit 的详细描述，可以分成多行。有两个注意点 : 
> - 使用第一人称现在时，比如使用change而不是changed或changes。
> - 应该说明代码变动的动机，以及与以前行为的对比。



### Footer

Footer 部分只用于两种情况.

- **不兼容改动**

    > 如果当前代码与上一个版本不兼容,则 Footer 部分 以 `BREAKING CHANGE` 开头, 后面是对变动的描述, 以及变动理由和迁移方法:

    ```shell
    BREAKING CHANGE: isolate scope bindings definition has changed and
        the inject option for the directive controller injection was removed.
        
        To migrate the code follow the example below:
        
        Before:
        
        scope: {
          myAttr: 'attribute',
          myBind: 'bind',
          myExpression: 'expression',
          myEval: 'evaluate',
          myAccessor: 'accessor'
        }
        
        After:
        
        scope: {
          myAttr: '@',
          myBind: '@',
          myExpression: '&',
          // myEval - usually not useful, but in cases where the expression is assignable, you can use '='
          myAccessor: '=' // in directive's template change myAccessor() to myAccessor
        }
        
        The removed `inject` wasn't generaly useful for directives so there should be no code using it.
    ```

- **关闭 Issue**

    ```shell
    Closes #112, #122, #132
    Fixed  #112, #122, #132
    ```





## 对于 Revert type 的 规范

> 如果当前 commit 用于撤销以前的 commit，则必须以 `revert:` 开头，后面跟着被撤销 Commit 的 Header

```shell
revert: feat(pencil): add 'graphiteWidth' option
 
This reverts commit 667ecc1654a317a13331b17617d973392f415f02.
```

Body部分的格式是固定的，必须写成`This reverts commit <hash>.`，其中的 hash 是被撤销 commit 的 SHA 标识符。如果当前 commit 与被撤销的 commit，在同一个发布（release）里面，那么它们都不会出现在 Change log 里面。如果两者在不同的发布，那么当前 commit，会出现在 Change log 的 `Reverts` 小标题下面。

