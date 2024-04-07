# 使用官方MySQL 8.0镜像作为基础镜像
FROM mysql:8.0

# 设置MySQL root用户的密码，可以使用ARG和ENV指令，这样可以在构建时通过--build-arg传递密码
ARG MYSQL_ROOT_PASSWORD
#ENV MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD
ENV MYSQL_ROOT_PASSWORD="minios"

# 设置MySQL的时区，例如设置为亚洲上海时区
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# 拷贝自定义的MySQL配置文件到容器中
COPY my.cnf /etc/mysql/conf.d/my.cnf

# 初始化MySQL数据目录权限和用户账户
RUN chown -R mysql:mysql /var/lib/mysql && \
    usermod -u 1000 mysql && groupmod -g 1000 mysql

# 若有初始化SQL脚本，可以拷贝到容器中，并在容器启动时自动执行
COPY init.sql /docker-entrypoint-initdb.d/

# 开放所需的端口
EXPOSE 3306
# 设置容器启动时执行的命令
CMD ["mysqld"]
