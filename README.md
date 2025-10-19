# SlideTemplate

犬戎的 MkSlides 主题。

预览：[https://inuebisu.github.io/SlideTemplate/](https://inuebisu.github.io/SlideTemplate/)

## 构建与部署

1. Clone 仓库：

    ```bash
    git clone https://github.com/inuEbisu/SlideTemplate.git
    ```

2. 安装依赖：

    ```bash
    npm install
    ```

3. 实时预览：

    ```bash
    make
    ```

4. 构建静态文件：

    ```bash
    make build
    ```

配置了 GitHub Workflow，每次提交均可自动部署至 GitHub Pages。

## 阅读

按 `?` 键查看快捷键。

## 开始写作

使用 [Prettier](https://prettier.io/) 进行格式化，CI 会检查格式化情况。每次 commit 前记得执行：

```bash
make format
```

## License

This project is licensed under the MIT License.
