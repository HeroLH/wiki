----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# 目录 {#index}

[TOC]











--------------------------------------------

# pages

> [Go静态代码检查工具GolangCI-Lint](https://www.pianshen.com/article/5426374939/)

&emsp;&emsp;`GolangCI-Lint` 是一个lint聚合器，它的速度很快，平均速度是 `gometalinter` 的 5 倍。它易于集成和使用，具有良好的输出并且具有最小数量的误报。而且它还支持 `go modules`。最重要的是免费开源。

![img](.assets/123.png)



# 安装

&emsp;&emsp;大多数安装都是为CI（continuous integration）准备的，强烈推荐安装固定版本的`golangci-lint`。

```shell
" 二进制文件将会被安装在$(go env GOPATH)/bin/golangci-lint目录
curl -sfL https://install.goreleaser.com/github.com/golangci/golangci-lint.sh | sh -s -- -b $(go env GOPATH)/bin vX.Y.Z

" 或者安装它到./bin/目录
curl -sfL https://install.goreleaser.com/github.com/golangci/golangci-lint.sh | sh -s vX.Y.Z

" 在alpine Linux中，curl不是自带的，你需要使用下面命令
wget -O - -q https://install.goreleaser.com/github.com/golangci/golangci-lint.sh | sh -s vX.Y.Z

```

上述命令执行完成后，你可以使用 `golangci-lint --version` 来查看它的版本。





# 使用

```shell
golangci-lint run [目录]/[文件名]
```



## 支持的linter

可以通过命令 `golangci-lint help linters` 查看它支持的linters。你可以传入参数 `-E/--enable`来使某个`linter`可用，也可以使用`-D/--disable`参数来使某个`linter`不可用。例如：

```shell
golangci-lint run --disable-all -E errcheck
```

