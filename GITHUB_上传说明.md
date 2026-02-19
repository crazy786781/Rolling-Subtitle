# 上传到 GitHub 的后续步骤

`.gitignore` 已添加，本地仓库需你本机执行一次初始化与提交，再在 GitHub 建仓并推送。

## 一、本地首次提交（二选一）

### 方式 A：运行批处理（推荐）

在项目根目录双击运行 **`git_init_and_commit.bat`**，按提示完成 `git init`、`git add`、`git commit`。

若从未配置过 Git 用户信息，先在本机执行一次：

```bash
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"
```

然后再运行 `git_init_and_commit.bat`。

### 方式 B：手动执行命令

在项目根目录打开 **命令提示符** 或 **PowerShell**（若你当前终端有报错，可尝试“以管理员身份”或从“开始菜单”直接打开 **cmd**），执行：

```powershell
cd "D:\我的文档\桌面\脚本及说明\滚动字幕_无ICL-GQ版"
git init
git add .
git status
git commit -m "Initial commit: 地震预警及情报实况栏程序"
```

## 二、仓库地址

本仓库已对应：**https://github.com/crazy786781/Rolling-Subtitle**

若尚未在 GitHub 上创建该仓库，请先到 [GitHub New repository](https://github.com/new) 创建名为 `Rolling-Subtitle` 的空仓库（不要勾选 README/.gitignore）。

## 三、关联远程并推送

**方式 A：双击运行 `git_push.bat`**（会自动添加 remote 并执行 push）

**方式 B：在项目根目录手动执行：**

```powershell
git remote add origin https://github.com/crazy786781/Rolling-Subtitle.git
git branch -M main
git push -u origin main
```

首次推送时若提示登录，按浏览器或终端提示完成 GitHub 认证即可。
