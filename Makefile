# 测试环境部署
dev:
	# 构建mysql环境
	# 运行后端
	docker build -t minios-dev .
	docker run -p 8000:8000 --name minios-django -d minios-dev

	# 运行前端

	# 配置nginx