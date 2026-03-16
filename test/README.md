# Django 教务管理示例项目（demo）

本项目是一个基于 **Django** 的教务/班级管理示例站点，包含学生、教师、班级（年级）等基础管理页面，并带有登录/注册能力；部分教师模块提供了简单的 API 接口（基于 Django REST Framework）。

## 功能概览

- **账号**：登录 / 注册 / 退出登录（基于 Django 自带认证系统）
- **学生管理**：列表、创建、更新、删除；支持筛选（`django-filter`）
- **教师管理**：列表、创建、更新、删除；提供简单 API（JSON）
- **班级/年级管理**：列表、创建、删除
- **页面模板与静态资源**：`templates/` 与 `static/` 已配置

## 技术栈

- **Python**：建议 3.10+（`Dockerfile` 使用 3.12）
- **Django**：项目由 Django 4.1 初始化（见 `demo/settings.py` 顶部说明）
- **数据库**：MySQL（`demo/settings.py` 里使用 `django.db.backends.mysql`）
- **可选/相关依赖**：
  - `django-filter`（学生列表筛选）
  - `djangorestframework`（教师 API 与序列化器使用）
  - `pymysql` 或 `mysqlclient`（二选一；用于连接 MySQL）

> 说明：当前仓库里未提供 `requirements.txt` / `pyproject.toml`。建议你后续补一个依赖清单，便于环境复现。

## 目录结构（核心）

```text
.
├─ demo/                # 项目配置（settings/urls/asgi/wsgi）
├─ main/                # 首页（渲染 home.html）
├─ account/             # 登录/注册/退出
├─ student/             # 学生管理（含 django-filter）
├─ teacher/             # 教师管理（含 DRF API）
├─ grade/               # 班级/年级管理
├─ try/                 # 试验页面
├─ templates/           # Django 模板
├─ static/              # 静态资源
├─ manage.py
└─ Dockerfile
```

## 路由入口

项目总路由位于 `demo/urls.py`，主要入口如下：

- **后台管理**：`/admin/`
- **首页**：`/`
- **登录/注册页入口**：`/login/`
- **学生模块**：`/student/`
- **教师模块**：`/teacher/`
  - 教师 API：`/teacher/api/`、`/teacher/api/<pk>/`
- **班级/年级模块**：`/grade/`
- **try 页面**：`/try/`
- **tailwind 示例页**：`/tailwind/`

## 本地运行（推荐开发方式）

### 1) 准备数据库（MySQL）

`demo/settings.py` 中默认数据库配置为：

- **DB**：`test`
- **USER**：`root`
- **PASSWORD**：`123456`
- **HOST**：`127.0.0.1`
- **PORT**：`3306`

请确保本机 MySQL 已启动，并创建数据库：

```sql
CREATE DATABASE test DEFAULT CHARACTER SET utf8mb4;
```

> 你也可以直接修改 `demo/settings.py` 中的 `DATABASES` 为自己的用户名/密码/库名。

### 2) 创建虚拟环境并安装依赖

在项目根目录执行（PowerShell 示例）：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -U pip
pip install django==4.1.* django-filter djangorestframework pymysql
```

> 若你更偏好 `mysqlclient`：需要额外安装编译依赖；Windows 上通常更省事的是先用 `pymysql`。

### 3) 初始化表结构并启动

```powershell
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

浏览器访问 `http://127.0.0.1:8000/`。

## Docker 运行

项目提供了 `Dockerfile`，默认会启动：

```text
python manage.py runserver 0.0.0.0:8000
```

构建与运行：

```powershell
docker build -t django-demo .
docker run --rm -p 8000:8000 django-demo
```

### Docker 下的数据库注意事项（很重要）

当前 `demo/settings.py` 的数据库 `HOST` 是 `127.0.0.1`：

- **在容器内**，`127.0.0.1` 指向的是“容器自身”，通常连不到你宿主机上的 MySQL。

可选处理方式：

- **方式 A（开发机 Windows 常用）**：把 `HOST` 改为 `host.docker.internal`
- **方式 B（更标准）**：新增 `docker-compose.yml`，起一个 `mysql` 服务，并将 `HOST` 改为服务名（例如 `db`）
- **方式 C**：将 MySQL 也跑在同一个容器内（不推荐）

## 开发备注

- **SECRET_KEY/DEBUG**：当前为开发配置（`DEBUG=True` 且 `SECRET_KEY` 写在代码里），仅用于本地学习/测试。
- **依赖声明**：建议补充 `requirements.txt`，例如：

```powershell
pip freeze > requirements.txt
```

## 常见问题

### 1) 报错找不到 `rest_framework`

教师模块使用了 DRF（`teacher/views.py`、`teacher/serializers.py`），请确认：

- 已安装：`pip install djangorestframework`
- 并在 `INSTALLED_APPS` 中加入：`rest_framework`（如你需要启用 DRF 的功能/页面）

---

如果你希望我顺手给这个项目补齐 `requirements.txt`，以及补一个可直接起 MySQL 的 `docker-compose.yml`（并把数据库配置改成可通过环境变量控制），我也可以直接帮你完善好。
