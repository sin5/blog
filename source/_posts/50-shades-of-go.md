---
title: 'Go 语言的 50 个陷阱'
categories:
  - 翻译
toc_excerpt: true
date: 2017-06-27 23:19:42
tags:
---
> 原文出自 [这里](http://devs.cloudimmunity.com/gotchas-and-common-mistakes-in-go-golang/index.html)

Go is a simple and fun language, but, like any other language, it has a few gotchas... Many of those gotchas are not entirely Go's fault. Some of these mistakes are natural traps if you are coming from another language. Others are due to faulty assumptions and missing details.
<code hide>Go 是一门简单而有趣的语言，但是，像其他语言一样，它有一些陷阱。。许多错误不是 Go 的问题，这其中一部分来自于其他语言对你的误导，而另一部分则是错误的猜想和遗漏的细节。</code>


A lot of these gotchas may seem obvious if you took the time to learn the language reading the official spec, wiki, mailing list discussions, many great posts and presentations by Rob Pike, and the source code. Not everybody starts the same way though and that's OK. If you are new to Go the information here will save you hours debugging your code.
<code hide></hide>

This post covers Go 1.5 and below.
