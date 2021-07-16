----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# Git Commit Message 编写规范 {#index}

[TOC]











## Git Commit Message 模板

### 使用注意事项:

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





## Git Commit Message 规范参照

### 目的

- 提供更多的历史信息,方便 `快速浏览` 和 `暂时回滚`

- 可以使用命令 `git log HEAD --pretty=format:%s`  预览此前的提交信息.

- 可以快速过滤某些 commit (比如文档改动) , 以便快速查找信息

- 可以直接从 commit 生成 Change Log (过滤出 feature 和 fix type 的 提交即可)



### 参考案例

-  [如何写好git commit message](https://www.cnblogs.com/deng-cc/p/6322122.html)
-  [阮一峰的网络日志：Commit message 和 Change log 编写指南](http://www.ruanyifeng.com/blog/2016/01/commit_message_change_log.html)
-  [写好 Git Commit 信息的 7 个建议](http://blog.jobbole.com/92713/)
-  [angular](https://github.com/angular/angular)
-  [commit-message-test-project](https://github.com/cpselvis/commit-message-test-project)
-  [babel-plugin-istanbul](https://github.com/istanbuljs/babel-plugin-istanbul)
-  [conventional-changelog](https://github.com/conventional-changelog/conventional-changelog)



### 总体方案

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



### 对 Header，Body，Footer的介绍

#### Header

Header 部分尽量只有一行, `<type>(<scope>): <subject>`  包括三个字段: `type`(必须) , `scope`(可选) , `subject`(必须)

##### type

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



##### scope

> `scope` 用于说明 commit 影响的范围, 比如 数据层, 控制层, 视图层...... , 视项目的不同而不同



##### subject

>  `subject` 是 commit 目的的简短描述 , 不超过50个字符

```shell
# 以动词开头,使用第一人称现在时, 比如 change, 而不是 changed 或者 changes
# 第一个字母小写
# 结尾不加句号
```



#### Body
> Body 部分是对本次 commit 的详细描述，可以分成多行。有两个注意点 : 
> - 使用第一人称现在时，比如使用change而不是changed或changes。
> - 应该说明代码变动的动机，以及与以前行为的对比。



#### Footer

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





### 对于 Revert type 的 规范

> 如果当前 commit 用于撤销以前的 commit，则必须以 `revert:` 开头，后面跟着被撤销 Commit 的 Header

```shell
revert: feat(pencil): add 'graphiteWidth' option
 
This reverts commit 667ecc1654a317a13331b17617d973392f415f02.
```

Body部分的格式是固定的，必须写成`This reverts commit <hash>.`，其中的 hash 是被撤销 commit 的 SHA 标识符。如果当前 commit 与被撤销的 commit，在同一个发布（release）里面，那么它们都不会出现在 Change log 里面。如果两者在不同的发布，那么当前 commit，会出现在 Change log 的 `Reverts` 小标题下面。





## Git 提交时的 emoji 表情使用指南

> [Git提交时的emoji表情使用指南——一波骚操作让你的Git提交更加生动](https://blog.csdn.net/weixin_34194551/article/details/91373327)

&emsp;&emsp;关于所有的emoji图标代码，可以参考 [emojipedia](https://link.juejin.im/?target=https%3A%2F%2Femojipedia.org%2F)，不过GitHub上有一套约定俗成的 emoji 使用规范，我整理成了以下表格，在使用git提交信息的时候，你不妨尝试使用它们，让你的提交信息更加明晰和生动。

```shell
git commit -m ":tada: Initial commit"
```

| emoji                                        | emoji 代码                    | commit 说明                  |
| :------------------------------------------- | :---------------------------- | :--------------------------- |
| :art: (调色板)                               | `:art:`                       | 改进代码结构/代码格式        |
| :zap: (闪电) :racehorse: (赛马)              | `:zap:` `:racehorse:`         | 提升性能                     |
| :fire: (火焰)                                | `:fire:`                      | 移除代码或文件               |
| :bug: (bug)                                  | `:bug:`                       | 修复 bug                     |
| :ambulance: (急救车)                         | `:ambulance:`                 | 重要补丁                     |
| :sparkles: (火花)                            | `:sparkles:`                  | 引入新功能                   |
| :memo: (备忘录)                              | `:memo:`                      | 撰写文档                     |
| :rocket: (火箭)                              | `:rocket:`                    | 部署功能                     |
| :lipstick: (口红)                            | `:lipstick:`                  | 更新 UI 和样式文件           |
| :tada: (庆祝)                                | `:tada:`                      | 初次提交                     |
| :white_check_mark: (白色复选框)              | `:white_check_mark:`          | 更新测试                     |
| :lock: (锁)                                  | `:lock:`                      | 修复安全问题                 |
| :apple: (苹果)                               | `:apple:`                     | 修复 macOS 下的问题          |
| :penguin: (企鹅)                             | `:penguin:`                   | 修复 Linux 下的问题          |
| :checkered_flag: (旗帜)                      | `:checked_flag:`              | 修复 Windows 下的问题        |
| :robot:（机器人）                            | `:robot:`                     | 修复 Android 下的问题        |
| :green_apple: (绿苹果)                       | `:green_apple:`               | 修复 iOS 下的问题            |
| :bookmark: (书签)                            | `:bookmark:`                  | 发行/版本标签                |
| :rotating_light: (警车灯)                    | `:rotating_light:`            | 移除 linter 警告             |
| :construction: (施工)                        | `:construction:`              | 工作进行中                   |
| :construction_worker: (工人)                 | `:construction_worker:`       | 添加 CI 构建系统             |
| :green_heart: (绿心)                         | `:green_heart:`               | 修复 CI 构建问题             |
| :arrow_up: (上升箭头)                        | `:arrow_up:`                  | 升级依赖                     |
| :arrow_down: (下降箭头)                      | `:arrow_down:`                | 降级依赖                     |
| :pushpin: (图钉)                             | `:pushpin:`                   | 将依赖项固定到特定版本       |
| :chart_with_upwards_trend: (上升趋势图)      | `:chart_with_upwards_trend:`  | 添加分析或跟踪代码           |
| :recycle: （回收）                           | `:recycle:`                   | 重构代码                     |
| :whale: (鲸鱼)                               | `:whale:`                     | Docker 相关工作              |
| :globe_with_meridians: (带子午线的地球仪)    | `:globe_with_meridians:`      | 国际化与本地化               |
| :heavy_plus_sign: (加号)                     | `:heavy_plus_sign:`           | 增加一个依赖                 |
| :heavy_minus_sign: (减号)                    | `:heavy_minus_sign:`          | 减少一个依赖                 |
| :wrench: (扳手)                              | `:wrench:`                    | 修改配置文件                 |
| :hammer: (锤子)                              | `:hammer:`                    | 重大重构                     |
| :pencil2: (铅笔)                             | `:pencil2:`                   | 修复 typo                    |
| :hankey: (粑粑...)                           | `:hankey:`                    | 写了辣鸡代码需要优化         |
| :rewind: (倒带)                              | `:rewind:`                    | 恢复更改                     |
| :twisted_rightwards_arrows: (交叉向右的箭头) | `:twisted_rightwards_arrows:` | 合并分支                     |
| :package: (包裹)                             | `:package:`                   | 更新编译的文件或包           |
| :alien: (外星人)                             | `:alien:`                     | 由于外部API更改而更新代码    |
| :truck: (货车)                               | `:truck:`                     | 移动或者重命名文件           |
| :page_facing_up: (正面朝上的页面)            | `:page_facing_up:`            | 增加或更新许可证书           |
| :boom: (爆炸)                                | `:boom:`                      | 引入突破性的变化             |
| :bento: (铅笔)                               | `:bento:`                     | 增加或更新资源               |
| :ok_hand: (OK手势)                           | `:ok_hand:`                   | 由于代码审查更改而更新代码   |
| :wheelchair: (轮椅)                          | `:wheelchair:`                | 改善无障碍交互               |
| :bulb: (灯泡)                                | `:bulb:`                      | 给代码添加注释               |
| :beers: (啤酒)                               | `:beers:`                     | 醉醺醺地写代码...            |
| :speech_balloon: (消息气泡)                  | `:speech_balloon:`            | 更新文本文档                 |
| :card_file_box: (卡片文件盒)                 | `:card_file_box:`             | 执行与数据库相关的更改       |
| :loud_sound: (音量大)                        | `:loud_sound:`                | 增加日志                     |
| :mute: (静音)                                | `:mute:`                      | 移除日志                     |
| :busts_in_silhouette: (轮廓中的半身像)       | `:busts_in_silhouette:`       | 增加贡献者                   |
| :children_crossing: (孩童通行)               | `:children_crossing:`         | 优化用户体验、可用性         |
| :building_construction: (建筑建造)           | `:building_construction:`     | 结构变动                     |
| :iphone: (iPhone)                            | `:iphone:`                    | 做响应式设计                 |
| :clown_face: (小丑脸)                        | `:clown_face:`                | 嘲弄事物（直译，这个没明白） |
| :egg: (鸡蛋)                                 | `:egg:`                       | 增加彩蛋                     |
| :see_no_evil: (看不见邪恶)                   | `:see_no_evil:`               | 增加或更改gitignore          |
| :camera_flash: (照相机闪光灯)                | `:camera_flash:`              | 增加或更新截图               |
| :alembic: (蒸馏器)                           | `:alembic:`                   | 尝试新东西                   |
| :mag: (放大镜)                               | `:mag:`                       | SEO优化                      |
| :wheel_of_dharma: (船的方向盘)               | `:wheel_of_dharma:`           | 关于Kubernetes的工作         |
| :label: (标签)                               | `:label:`                     | 增加类型（FLow、Typescript） |

以上表格由我整理并翻译自[Git Emoji](https://link.juejin.im/?target=https%3A%2F%2Fgitmoji.carloscuesta.me%2F)， 我们来一起作出更生动的Git 提交吧
