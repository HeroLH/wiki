----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# {Title} {#index}

[TOC]



 







--------------------------------------------

## 文档版本

|    时间    | /修改人 | 内容     |
| :--------: | :-----: | :------- |
| 2021-05-25 | Herolh  | 文档创建 |
|            |         |          |



## 简介

FSM 是 Go 的有限状态机。

它很大程度上基于两种 FSM 实现：

- JavaScript 有限状态机[javascript-state-machine](https://github.com/jakesgordon/javascript-state-machine)
- 适用于 Python 的 [oxplot/fysom](https://github.com/oxplot/fysom)（在[mriehl/fysom](https://github.com/mriehl/fysom)上分叉）

有关 API 文档和示例，请参见http://godoc.org/github.com/looplab/fsm



### 安装

```shell
go get github.com/looplab/fsm
```





## 基本使用

### hello world

```go
type Door struct {
	To  string
	FSM *fsm.FSM
}

func NewDoor(to string) *Door {
	d := &Door{
		To: to,
	}

	d.FSM = fsm.NewFSM(
		"closed",				//  初始状态
		fsm.Events{
			// 		标识					当前状态			转变成的状态
			{Name: "open", Src: []string{"closed"}, Dst: "open"},
			{Name: "close", Src: []string{"open"}, Dst: "closed"},
		},
		fsm.Callbacks{
			// key 有固定值，不是随便起的
			"enter_state": func(e *fsm.Event) { d.enterState(e) },
		},
	)
	return d
}

func (d *Door) enterState(e *fsm.Event) {
	fmt.Printf("The door to %s is %s\n", d.To, e.Dst)
}

func main() {
	// 创建door对象
	door := NewDoor("heaven")
	// 状态改变，此时对应fsm.Events中的Name：open状态，此时状态由closed转变为open
	// 然后调用回调函数 d.enterState(e),打印出当时状态
	err := door.FSM.Event("open")
	if err != nil {
		fmt.Println(err)
	}
	err = door.FSM.Event("close")
	if err != nil {
		fmt.Println(err)
	}
}
```

然后进行深一层次，丰富状态机转变时对应回调函数的调用及执行，类似 java 中拦截器，状态转变之前执行对应 before_xxx 的函数，

执行完后执行 leave_state 的函数，代码：

```go
func main() {
	//创建一个状态机
	//三个参数：1.默认状态 2.定义状态事件 3.定义状态转变时调用的函数
	fsm := fsm.NewFSM(
		"green",
		fsm.Events{
			//状态事件的名称   该事件的起始状态Src         该事件的结束状态Dst
			//即：状态事件warn（警告事件）表示事物的状态从状态green到状态yellow
			{Name: "warn", Src: []string{"green"}, Dst: "yellow"},
			{Name: "panic", Src: []string{"yellow"}, Dst: "red"},
			{Name: "yellow", Src: []string{"red"}, Dst: "blue"},
			{Name: "calm", Src: []string{"red"}, Dst: "yellow"},
		},
		//状态事件调用函数，在此称为 时机函数。关键字用'_'隔开，格式是："调用时机_事件或状态"
		//before表示在该事件或状态发生之前调用该函数，如"before_warn"，表示在warn
		//这个状态事件发生前调用这个函数。"before_yellow"表示进入yellow状态之前调用
		//该函数。
		//依此类推，after表示在...之后，enter表示在进入...之时，leave表示在离开...
		//之时。
		fsm.Callbacks{
			//fsm内定义的状态事件函数，关键字指定的是XXX_event和XXX_state
			//表示任一的状态或状态事件
			"before_event": func(e *fsm.Event) {
				fmt.Println("before_event")
			},
			"leave_state": func(e *fsm.Event) {
				fmt.Println("leave_state")
			},
			//根据自定义状态或事件所定义的状态事件函数
			"before_yellow": func(e *fsm.Event) {
				fmt.Println("before_yellow")
			},
			"before_warn": func(e *fsm.Event) {
				fmt.Println("before_warn")
			},
		},
	)
	//打印当前状态，输出是默认状态green
	fmt.Println(fsm.Current())
	//触发warn状态事件，状态将会从green转变到yellow
	//同时触发"before_warn"、"before_yellow"、"before_event"、"leave_state"函数
	fsm.Event("warn")
	fmt.Println("======================")
	fsm.Event("panic")
	fmt.Println("======================")
	fsm.Event("yellow")
	//打印当前状态，输出状态是yellow
	fmt.Println(fsm.Current())
}
```

