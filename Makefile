# 测试环境部署，前后端数据库都运行
dev:
	# 构建通信网络
	docker network create minios_network

	# 构建mysql环境

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

# 一键部署生产环境
prod:
	echo "前端启动地址：http://localhost:3000"