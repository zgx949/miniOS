# 构建通信网络
.PHONY: check-minios-network
check-minios-network:
ifeq ($(shell docker network inspect minios_network 2>/dev/null | grep Name),)
	docker network create minios_network
endif
# 测试环境部署，前后端数据库都运行
dev:
	# 检查内网是否构建
	@if [ -z "$$(docker network inspect minios_network 2>/dev/null)" ]; then \
        docker network create minios_network; \
    fi
	# 构建mysql环境
	docker build -t minios-mysql-dev ./mysql
	docker run -p 3306:3306 --name minios-mysql -d --network=minios_network minios-mysql-dev

	# 运行后端
	docker build -t minios-django-dev .
	docker run -p 8000:8000 --name minios-django -d --network=minios_network minios-django-dev

	# 运行前端
	docker build -t minios-vue-dev ./vue/mini_os/
	docker run -p 3000:3000 --name minios-vue-dev -d --network=minios_network minios-vue-dev
	# 配置nginx

# 只运行后端
run-backend:
	#docker build -t minios-django-dev .
	docker run -p 8000:8000 --name minios-django -d --network=minios_network minios-django-dev

# 只运行前端
run-frontend:
	#docker build -t minios-vue-dev ./vue/mini_os/
	docker run -p 3000:3000 --name minios-vue-dev -d --network=minios_network minios-vue-dev
	echo "前端启动地址：http://localhost:3000"

# 只运行mysql
run-mysql:
	# 构建mysql环境
	#docker build -t minios-mysql-dev ./mysql
	docker run -p 3306:3306 --name minios-mysql -d --network=minios_network minios-mysql-dev

# 一键部署生产环境
prod:
	docker-compose up -d
	echo "前端启动地址：http://localhost"