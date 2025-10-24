---
title: "Lec 1. 正确地在计算机学院生存"
---

# Lec 1. 正确地在计院生存

<hr>

2025 年秋冬学期计算机学院朋辈辅学「技能拾遗」

<div class="avatar-container">
<a href="https://github.com/inuEbisu"><img class="avatar-img" src="avatar_512.png" alt="avatar"></a>
<span class="avatar-name">@inuEbisu / 犬戎</span>
</div>

2025 年 10 月 24 日

---

## Part 1. 学习的态度

-v-

### 端正态度

> 这种「只要不影响我现在 survive，就不要紧」的想法其实非常的利己和短视：你在专业上的技不如人，迟早有一天会找上来，会影响到你个人职业生涯的长远的发展。教育除了知识的记忆之外，更本质的是能力的训练，即所谓的 training；而**但凡 training 就必须克服一定的难度**，否则你就是在做重复劳动，能力也不会有改变。如果遇到难度就选择退缩，或者让别人来替你克服本该由你自己克服的难度，等于是自动放弃了获得 training 的机会；而这，其实是大学专业教育最宝贵的部分。
>
> <div style="text-align: right;"> —— Etone</div>

-v-

### 端正态度

> 大家在学习的过程中会遇到各种各样的问题，伴随而来的可能还会有相当程度的挫败感和焦虑感，这些是大家或多或少都会经历的。因此我们计划在培养学生们的技术水平和科研能力之外，更重要的是教会大家如何用一种平常心去对待这些问题：**当我们去做难度大且有意义的事情时，不好解决的问题必然是客观存在的，当然解决问题的方法也是一定存在的。**既然问题和解决方法都始终存在，我们何必殚精竭虑地自怨自艾呢？取而代之的是，我们应该放平心态且对自己充满自信，努力从一次次失败中总结经验。通过几次正向反馈，大家不仅能收获满满的成就感，心理素质也会得到很好的锤炼。
>
> <div style="text-align: right;"> —— <a href="https://ysyx.oscc.cc/">《一生一芯》项目介绍</a></div>

-v-

### 端正态度

在计算机的世界中

- 机器永远是对的

- 世界上没有魔法

所以我们要使用**科学的方法**来解决问题

- ATFAI, STFW, RTFM, RTFSC

- Debug and Profile

- 扎实学习基础知识

-v-

### 持之以恒

知识体系是螺旋上升的

- [Mathematical Maturity](https://en.wikipedia.org/wiki/Mathematical_maturity)

- 神经科学

> 坚持一年，你就会发现有不同；坚持两年，你就会发现大有不同。
>
> <div style="text-align: right;"> —— 陈道蓄</div>

-v-

### 实践

> 实践是检验真理的唯一标准

> 行在知之前

- 计算机是工科

- 多写代码

- 现在想要 DFS 式学习非常方便
    - Just ATFAI

    - And spend time

---

## Part 2. ATFAI

-v-

### 通常的做法

- ATFAI (**A**sk **T**he **F**ucking **A**rtificial **I**ntelligence)

- STFW (**S**earch **T**he **F**ucking **W**eb)

- RTFM (**R**ead **T**he **F**ucking **M**anual)

- RTFSC (**R**ead **T**he **F**ucking **S**ource **C**ode)

时间上的先后关系，前面的方法是后面的方法的偷懒

- 最后再考虑提问

<!-- - 例如当搜索互联网解决不了问题时，你应当去看手册

- 不要许愿，不要祈祷，使用**科学的方法**解决问题

- 如果都解决不了，最后考虑提问 -->

-v-

### AI 何物

ATFAI: **A**sk **T**he **F**ucking **A**rtificial **I**ntelligence

AI 发展太快了！

> 回想一下，DeepSeek R1 出世是什么时候的事情？

GPT-5 很强

-v-

### 选择你的英雄

- GPT-5

- Gemini 2.5 Pro

- Claude Sonnet 4.5
    - 长于中文写作

- DeepSeek V3/R1
    - 免费且模型开放

大模型厂商很喜欢宣传

自己去试一试

（只用过豆包 / Kimi？）

-v-

### AI-IDE

- VSCode Copilot
    - GitHub Pro

    - CC98: [Github Education / Copilot Pro 学生认证 / 教育优惠申请完全教程](https://www.cc98.org/topic/6182140)

- Cursor

- Trae

- AI CLI + Unix Philosophy

-v-

### 使用 AI DFS 式学习

不断地追问

妙妙 Prompt：

> 你是一位〇〇领域的专业人士。我现在想要〇〇〇〇。
>
> 我可以如何将这件事做得更专业一些？

-v-

### 试一试

1. `fork.py`

2. 将递归代码转化为非递归代码
   `recursion.py`

---

## Part 3. STFW

-v-

### Steam 玩家

有一天你听同学说，Steam 上有很多游戏可以玩

-v-

### 选择你的英雄

<div class="mul-cols">
<div class="col">

- ~~百度~~

- Bing

- Google

</div>

<div class="col">

- ~~百度百科~~

- Wikipedia

</div>

<div class="col">

- 知网

- Google Scholar

- Semantic Scholar

</div>

</div>

魏则西

-v-

### 搜索引擎的原理

- 分词 (Tokenization)

- 去除停用词 (Stop Words)

- 倒排索引

- 排序 (PageRank 等)

> To be or not to be, that is the question

-v-

### 搜索引擎的原理

> 为我出于该课程的教学目的，用 Python 实现一个简单的搜索引擎的前半部分（输入查询文本，包含 Tokenization 与 Stop Words 去除流程，输出处理后的 list），供我演示搜索引擎的基本原理。简洁明了为主，不必添加冗长的注释与异常处理，可以使用你想使用的任何库（例如 jieba 等）。

GPT-5: `preprocess.py`

-v-

### 分词

- 如何在 Python 中读取文件

- Python 读取文件

- Python read file

<br>

- 我遇到了段错误，我应该怎么办？

- 段错误

- Segmentation Fault core dumped

-v-

### 搜索引擎的奇技淫巧

| 语法          | 用法                                   | 样例                           |
| :------------ | :------------------------------------- | :----------------------------- |
| 引号 `"word"` | 搜索​​完整词组​​，忽略词形变化和同义词 | `"机器学习入门"` / `"guthib"`  |
| 减号 `-word`  | 排除关键词                             | `-site:blog.csdn.net`          |
| `site:`       | 限定域名​​                             | `site:edu` / `site:github.com` |
| `​filetype:`  | 限定文件类型​                          | `filetype:pdf`                 |
| `​intitle:`   | 限定在标题中                           | `intitle:"Computer Science"`   |
| `intext:`     | 限定在正文中                           | `intext:`                      |
| `​inurl:​​`   | 限定在 URL 中                          | `inurl:login`                  |

-v-

### 搜索结果质量

1. 官方文档 > 他人博客

2. Stack Overflow, GitHub Issues > 百度知道

3. 发布时间：近期文章 > 老旧博客

4. 语言：英文资源 > 博客园 > CSDN > 机翻中文内容农场
    - CSDN 其实活人不少

-v-

### 试一试

- 搜索操作系统教程

- 搜索一个 C 语言的红黑树实现

- 搜索浙江大学奖学金

---

## Part 4. RTFM

-v-

### Manual

常指 Linux 下的命令 `man`

当然也可以指：

- 官方文档

- 语言规范

- 学术论文

- 请求意见稿 (RFCs)

-v-

### Linux man

知道「手册」的存在

- 系统上的一手资料

- 不需要网络

- 速度与专注

-v-

### man 的历史

- 最早的 man 手册于 ​​1971 年​​出现在 AT&T 的 ​​Unix 第一版​​中
    - Dennis Ritchie 与 Ken Thompson​​

    - 最初仍是纯文本

- 标准化的章节划分系统

- 被 Linux 社区继承与发扬
    - `man-pages`

-v-

### 使用 Manual

操作逻辑与 Vim 相近

- `man man`

-v-

### 使用 Manual

- `man ls`

- `man su`

- `man strcmp`

- `man kill`
    - `man 2 kill`

-v-

### TL;DR

`tldr`

- 社区贡献

- 联网
    - 有点慢

-v-

### TL;DR

- `tldr ls`

- `tldr tar`

-v-

### 试一试

1. 查阅 `man` 查看 `gcc` 编译选项
    - 用 `tldr` 再试一试

2. 查阅 `man` 来了解刚刚遇到的系统调用 `fork`

---

## Part 5. RTFSC

-v-

### Source Code

> Talk is cheap, show me the code

- Manual 可能过时，博客可能出错

- 代码永远告诉你它实际上在做什么
    - 具体方式

    - 复杂度与代价

- 理解实现细节，理解接口

- 学习最佳实践和设计模式

-v-

### 让 AI 读

可以使用你的 AI-IDE

-v-

### 试一试

1. 探索 `preprocess.py` 做了什么
    - 可以进一步地探索 `jieba.lcut()` 的奥秘

2. 探索 `sorted()` 与 `list.sort()` 的区别

3. 探索 Flask 中的 `@app.route('/')` 装饰器如何工作的

---

## Part 6. 科学地提问

-v-

### 为什么不直接问

我们的目标是**解决问题**，而提问实际上**效率并不高**

- 每个人的机器与环境、每个人会犯的错误都不尽相同
    - 所以你遇到的问题老师和助教并不一定遇到过

    - 于是他们其实也是 ATFAI, STFW, RTFM, RTFSC

    - 那不如你自己来

- 提出问题 -> 助教解答 -> 自己解决，整个过程时间很长

- 如果提问的对象不是老师和助教，可能会没人理

<!-- 所以，首先 ATFAI, STFW, RTFM, RTFSC -->

-v-

### 提问前的自我审查

- ATFAI, STFW, RTFM, RTFSC 都尝试过了吗？
    - 这也是一个帮助你明确问题的过程

    - 「科学地提问」也同样适用于对 AI 提问
        - 给它尽可能多的信息

- 问题是否具体明确，你想知道/解决的究竟是什么？

-v-

### X-Y Problem

- Q: 我怎么用 Shell 取得一个字符串的后 3 位字符？
- A: 如果这个字符的变量是 `$foo`，你可以 `echo ${foo:-3}`。
- A: 为什么你要取后 3 位？你想干什么？
- Q: 其实我就想取文件的扩展名。
- A: 我靠，原来你要干这事，那我的方法不对，文件的扩展名并不保证一定有 3 位啊。
- A: 如果你的文件必然有扩展名的话，你可以 `echo ${foo##*.}`。

> 你试图做 X，并想到了用 Y 方案。所以你去问别人 Y，但根本不提 X。于是，你可以会错过本来可能有更好更适合的方案，除非你告诉大家 X 是什么。

把我们想解决的问题和整个事情的来龙去脉说清楚。

-v-

### 如何提问

@45gfg9: [我在图灵信安的两年半](https://www.cc98.org/topic/6092480)

在提问时至少保持基本的社交礼仪

<div class="mul-cols">
<div class="col">

> 作业是什么

> 有截止日期吗，啥时候

> 我电脑在修做不了咋办

</div>
<div class="col">

> 哦

> 我不能理解

> <img src="lec1/sweating_soy.png" style="margin: 0;"></img>

</div>
</div>

- 当然绝大多数同学都很好

-v-

### 如何提问

[提问的智慧（概要版）](https://soc.ustc.edu.cn/Digital/2025/lab0/ask/)

- 最重要的是描述清楚你的症状，问一个让人听得懂的问题

-v-

### 如何提问

> [拍屏] 助教，报错了，怎么办？这是什么情况，急急急

> 助教您好，我正在尝试实现 AVL 树的左旋操作。我期望在对节点 X 左旋后，它的右孩子 Y 会成为新的根。但程序在运行时出现了段错误。这是我的左旋函数和复现该问题的主函数代码。报错信息是 Segmentation fault (core dumped)。我怀疑是 `y->left = x;` 这一行指针操作有问题，但不太确定。我已经询问过 AI，也尝试过使用 gdb 单步调试，无果。我的环境是 Ubuntu 22.04, g++ 15.2.1。

---

## Part 7. 参考资料

-v-

### 参考资料

关于大学生活

- [上海交通大学生存手册](https://survivesjtu.gitbook.io/survivesjtumanual)
    - 可能需要用一整个学生时代甚至一生去读懂

- [如何自学](https://zhuanlan.zhihu.com/p/8050878695)
    - 其中不少内容普适

    - 催人奋进

- [CS 自学指南](https://csdiy.wiki/)
    - 上一节课就推了的东西，这一节课还是要推

-v-

### 参考资料

持之以恒

- 《刻意练习》，[美] K. Anders Ericsson

面向和我一样的 ADHD 患者的时间管理

- [手把手教你成为时间管理大师](https://www.cc98.org/topic/5852429)

- [自制力硬核技术讨论](https://zhuanlan.zhihu.com/p/1930893902623245386)

-v-

### 参考资料

RTFM

- [man 快速入门 - NJU ICS PA](https://nju-projectn.github.io/ics-pa-gitbook/ics2020/man.html)

- [man 文档的一些示例 - Linux 101](https://101.lug.ustc.edu.cn/Appendix/man/)

科学地提问

- [提问的智慧（概要版）](https://soc.ustc.edu.cn/Digital/2025/lab0/ask/)
- [提问的智慧](https://github.com/ryanhanwu/How-To-Ask-Questions-The-Smart-Way/blob/main/README-zh_CN.md)

- [别像弱智一样提问](https://github.com/tangx/Stop-Ask-Questions-The-Stupid-Ways)

- [Wikipedia: XY Problem](https://en.wikipedia.org/wiki/XY_problem)

---

# 谢谢大家

<hr>

Questions?

<div class="avatar-container">
<a href="https://github.com/inuEbisu"><img class="avatar-img" src="avatar_512.png" alt="avatar"></a>
<span class="avatar-name">@inuEbisu / 犬戎</span>
</div>

2025 年 10 月 24 日
