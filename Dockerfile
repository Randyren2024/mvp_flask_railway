# 使用轻量级 Python 基础镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 设置环境变量，防止 Python 生成 .pyc 文件以及启用无缓冲日志输出
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 安装系统依赖（如果需要）
# RUN apt-get update && apt-get install -y --no-install-recommends gcc && rm -rf /var/lib/apt/lists/*

# 复制依赖文件并安装
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码
COPY . .

# Railway 默认会注入 PORT 环境变量
ENV PORT 5000

# 启动应用，使用 gunicorn
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:$PORT app:app"]
