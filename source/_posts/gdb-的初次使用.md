---
title: gdb 的初次使用
date: 2017-04-16 21:57:05
tags:
- clang
- gdb
- apue
---

起因
---
阅读 apue, 默写<1.1-简单ls实现>, 运行报段错误, 错误代码如下：
```c
#include "apue.h"
#include <string.h>
#include <dirent.h>

int
main(int argc, char *argv[])
{
  DIR *dp;
  struct dirent *dir;

  if (argc != 2) {
    err_quit("usage: ls directory_name");
  }

  if ((dp = opendir(argv[1]) == NULL)) {
    err_quit("can't open directory %s", argv[1]);
  }

  while ((dir = readdir(dp) != NULL)) {
    printf("%s\n", dir->d_name);
  }
  return 0;
}
```
<!--more-->

经过
---
一时兴起, 想用 gdb 分析一下尸体.
1. `ulimit -c unlimited` 允许当前shell(bash)启动的进程输出core文件;
2. `1.1-ls /tmp` 制造一个尸体.
3. `gdb 1.1-ls core.16835` 开始观察.

> gdb 可能会提示某些依赖缺失, 安装即可.


观察到报错内容如下:
```
Program terminated with signal 11, Segmentation fault.
#0  0x00000034e58a8936 in __readdir (dirp=0x0) at ../sysdeps/unix/readdir.c:45
45	  __libc_lock_lock (dirp->lock);
```
明显看出是 readdir 时传入了空指针.
回顾代码发现, 因为 `dp = opendir(argv[1]) == NULL` 这句代码先将 opendir 的结果和 NULL 进行了比较, 之后将值付给了 dp.
由于 /tmp 文件存在, opendir 返回值不为 NULL, dp 被赋值 false, 隐式转换为指向 0x0 的指针.


另外 `dir = readdir(dp) != NULL` 存在同样问题.


结果
---
正确代码如下:
```
#include "apue.h"
#include <string.h>
#include <dirent.h>

int
main(int argc, char *argv[])
{
  DIR *dp;
  struct dirent *dir;

  if (argc != 2) {
    err_quit("usage: ls directory_name");
  }

  if ((dp = opendir(argv[1])) == NULL) {
    err_quit("can't open directory %s", argv[1]);
  }

  while ((dir = readdir(dp)) != NULL) {
    printf("%s\n", dir->d_name);
  }
  return 0;
}
```


gdb 是个强大的调试工具, 这里只是简单地看了下引发崩溃的调用, 更多的用法将在以后的学习过程中记述.
