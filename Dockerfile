 # 建立 python3.9 环境
FROM python:3.9
 

 # 设置 python 环境变量
ENV PYTHONUNBUFFERED 1
 
 # 设置pip源为国内源
COPY pip.conf /root/.pip/pip.conf
 
 # 在容器内/var/www/html/下创建 mysite1文件夹
RUN mkdir -p /app
 
 # 设置容器内工作目录
WORKDIR /app
 
 # 将当前目录文件加入到容器工作目录中（. 表示当前宿主机目录）
ADD . /app
 
 # 利用 pip 安装依赖
RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN chmod 777 django-run.sh

CMD "./django-run.sh"

EXPOSE 8000
