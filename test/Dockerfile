FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# 安装系统依赖（如需要可以在这里加上 gcc、libpq 等）
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    pkg-config \
    libmariadb-dev-compat \
    && rm -rf /var/lib/apt/lists/*

# 把项目代码复制到容器
COPY . /app

# 如果你有 requirements.txt，优先使用
# 没有的话，简单直接从 venv 里导出依赖（可根据需要修改/删除）
RUN if [ -f "requirements.txt" ]; then \
      pip install --no-cache-dir -r requirements.txt; \
    else \
      pip install --no-cache-dir django djangorestframework pymysql django-filter; \
    fi

# Django 默认运行端口
EXPOSE 8000

# 进入 demo 项目目录运行开发服务器（按你项目的 settings 配置来）
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

