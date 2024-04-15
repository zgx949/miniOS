# 使用官方的Nginx基础镜像
FROM nginx:latest

# 设置工作目录
WORKDIR /etc/nginx/conf.d

# 复制自定义的Nginx配置文件到容器中
COPY default.conf /etc/nginx/conf.d/default.conf

# 替换默认的Nginx配置
# RUN rm /etc/nginx/conf.d/default.conf

# 暴露端口80用于对外提供服务
EXPOSE 80

# 定义容器启动时执行的命令
CMD ["nginx", "-g", "'daemon off;'"]