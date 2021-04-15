----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# Elastic Search 基础使用 {#index}

[TOC]











--------------------------------------------

## 预备知识
### 教程

[bilibili - 狂神说 - ElasticSearch7.6.x 最新完整教程通俗易懂](https://www.bilibili.com/video/BV17a4y1x7zq)
[知乎 - 狂神说 ElasticSearch 学习笔记 + 补充](https://zhuanlan.zhihu.com/p/268065286)
[CSDN - 狂神说 ElasticSearch 入门（最全笔记）](https://blog.csdn.net/qq_21197507/article/details/115076913)



### 基石 Lucene

&emsp;&emsp;Doug Cutting 是一位美国工程师，他做了一个用于文本搜索的函数库，命名为 Lucene。**Lucene** 是用 java 写的，目标是为各种中小型应用软件加入全文搜索功能。
&emsp;&emsp;==Lucene 是一套信息检索工具包，并不包含搜索引擎系统==，它包含了索引结构、读写索引工具、相关性工具、排序等功能。因此在使用 Lucenen 时仍需关注搜索引擎系统，例如数据获取、解析、分词等方面的东西。
&emsp;&emsp;该项目早期被发布在 Doug Cutting 的个人网站，后来成为了 Apache 软件基金会 jakarta 项目的一个子项目。后来在 Lucene 的基础上开发了一款可以代替当时的主流搜索的开源搜索引擎，命名为 Nutch.

![image-20210415233516767](.assets/image-20210415233516767.png)

&emsp;&emsp;**Nutch** 是一个建立在 Lucene 核心之上的网页搜索应用程序，它在 Lucene 的基础上加了爬虫和一些网页相关的功能，目的就是从一个简单的站内检索推广到全球网络上的搜索上。随着时间的推移，作为互联网搜索引擎，都面临对象 "体积" 不断增大的问题。需要存储大量的网页，并不断优化自己的搜索算法，提升搜索效率。<u>大数据的两个问题: 存储 + 计算!</u>

&emsp;&emsp;在 2003 年， google 发表了一篇技术学术论文，公开介绍了自己的 google 文件系统 **GFS( Google File System )**。这是 google 公司为了==存储==海量搜索数据而设计出来的专用文件系统。

![image-20210415232805233](.assets/image-20210415232805233.png)

&emsp;&emsp;在 2004 年，Doug Cutting 基于 Google 的 GFS 论文实现了分布式文件存储系统，并将它命名为 **NDFS(Nutch Distributed File System)**。同年 google 又发表了一篇技术学术论文， 介绍自己的 **MapReduce 编程模型**，这个编程模型，用于大规模数据集( 1TB )的并行分析==运算==。

![image-20210415232825855](.assets/image-20210415232825855.png)

&emsp;&emsp;在 2005 年 Doug Cutting 基于 Google 的 MapReduce 在 Nutch 上实现了该功能。

![image-20210415231834143](.assets/image-20210415231834143.png)

&emsp;&emsp;在 2006 年 Doug Cutting  加入了雅虎，将 NDFS 和 MapReduce 进行了改造，并重新命名为 **Hadoop** (NDFS 也改名为 HDFS,Hadoop Distributed File System)* 这就是大名鼎鼎的大数据框架系统 Hadoop 的由来，而 Doug Cutting 则被人称为 Hadoop 之父。
&emsp;&emsp;在 2006 同年, Google 发表论文介绍自己的 **BigTable**, 一种分布式素据存储系统，用来处理海量数据的非关系型数据库。Doug Cutting 在自己的 hadoop 系统中，引入了 BigTable ，并命名为 **HBase**。

![image-20210415232728277](.assets/image-20210415232728277.png)

&emsp;&emsp;在 2008 年1月，Hadoop 正式成为 Apache 基金会的顶级项目。同年 2 月，Yahoo 宣布建成一个拥有 1 万个内核的 Hadoop 集群，并将自己的搜索引擎部署在上面。同年 7 月，Hadoop 打破世界记录，成为最快排序 1 TB数据的系统， 用时 209 秒。



### ElasticSearch 概述

&emsp;&emsp;ElasticSearch, 简称 es，==es 是一个开源的高拓展的分布式全文检索引擎==，它可以近乎实施的存储、检索数据；本身扩展性很好，可以扩展到上百台服务器，处理 PB 级别的数据。es 也==使用 java 开发并使用 Lucene 作为其核心==来实现所有索引和搜索的功能，但是它的目的是<u>通过简单的 RESTful API 来隐藏 Lucene 的复杂性</u>，从而让全文搜索变得简单。

