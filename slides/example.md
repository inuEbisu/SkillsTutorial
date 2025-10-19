---
title: "MkSlides Template"
---

# MkSlides Template

<hr>

<div class="avatar-container">
<a href="https://github.com/inuEbisu"><img class="avatar-img" src="avatar_512.png" alt="avatar"></a>
<span class="avatar-name">@inuEbisu / 犬戎</span>
</div>

---

## Part 1. Elements

-v-

### Code Block

```rust
fn main() {
    println!("Hello, World!");
}
```

```hs
primes = filterPrime [2..] where
  filterPrime (p:xs) =
    p : filterPrime [x | x <- xs, x `mod` p /= 0]
```

-v-

### List

- list 1
- list 2
    - list 2.1
        - list 2.1.1
        - list 2.1.2
    - list 2.2
        - list 2.2.1
- list 3
    - list 3.1
    - list 3.2
        - list 3.2.1
            - list 3.2.1.1
            - list 3.2.1.2
        - list 3.2.2
        - list 3.2.3

-v-

### Blockquote

> Classes teach you all about advanced topics within CS, from operating systems to machine learning, but there’s one critical subject that’s rarely covered, and is instead left to students to figure out on their own: proficiency with their tools. We’ll teach you how to master the command-line, use a powerful text editor, use fancy features of version control systems, and much more!
>
> Students spend hundreds of hours using these tools over the course of their education (and thousands over their career), so it makes sense to make the experience as fluid and frictionless as possible. Mastering these tools not only enables you to spend less time on figuring out how to bend your tools to your will, but it also lets you solve problems that would previously seem impossibly complex.

-v-

### Table

左对齐表格

| 表头 A           | 表头 B           | 表头 C |
| ---------------- | ---------------- | ------ |
| 这是一段内容     | 这里也是一段内容 | ...    |
| 这里是另一段内容 | ...              | ...    |

居中表格

|      表头 A      |      表头 B      | 表头 C |
| :--------------: | :--------------: | :----: |
|   这是一段内容   | 这里也是一段内容 |  ...   |
| 这里是另一段内容 |       ...        |  ...   |

-v-

### $\LaTeX$ Formula (i)

假设 $\sum_{n=1}^\infty a_n$ 是一个条件收敛的无穷级数。对任意的一个实数 $C$ ，都存在一种从自然数集合到自然数集合的排列 $\sigma : n \mapsto \sigma (n)$，使得

$$
  \sum_{n=1}^\infty a_{\sigma (n)} = C.
$$

此外，也存在另一种排列 $\sigma' : n \mapsto \sigma' (n)$ ，使得

$$
  \sum_{n=1}^\infty a_{\sigma' (n)} = \infty.
$$

类似地，也可以有办法使它的部分和趋于 $-\infty$ ，或没有任何极限。

-v-

### Image

<div class="mul-cols">
<div class="col">

Normal image

<img src="avatar_512.png" width="256" height="256"></img>

</div>
<div class="col">

Image with link

<a href="https://google.com/"><img src="avatar_512.png" width="256" height="256"></img></a>

</div>
</div>
---

## Part 2. Layout

-v-

### Multi-columns (i)

<div class="mul-cols">
<div class="col">

Column 1

- list
- list

</div>
<div class="col">

Column 2

```python
class MyClass:
    def __init__(self, ...):
        ...
    def method(self, ...):
        ...
```

</div>
</div>

-v-

### Multi-columns (ii)

<div class="mul-cols">
<div class="col">

第一列

- 列表
- 列表

</div>
<div class="col">

第二列

1. 列表
2. 列表
    - 列表

</div>
<div class="col">

第三列

```python
class MyClass:
    def __init__(self, ...):
        ...
    def method(self, ...):
        ...
```

</div>
</div>
