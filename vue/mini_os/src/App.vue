<script setup>
	// This starter template is using Vue 3 <script setup> SFCs
	// Check out https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup
	import HelloWorld from './components/HelloWorld.vue'
	import Left from './components/Left.vue'
	import Right from './components/Right.vue'
	import Nav from './components/Nav.vue'
	import {
		ElMessage,
		ElMessageBox
	} from 'element-plus'
	import {
		ref
	} from 'vue'
</script>

<template>
	<!-- <img alt="Vue logo" src="./assets/logo.png" />
  <HelloWorld msg="Hello Vue 3 + Vite" /> -->
	<el-watermark :font="font" :content="['左手文件系统']">


		<div class="header">
			<h1>左手网盘-Windows13版</h1>
		</div>

		<el-row :gutter="10">
			<el-col :xs="24" :sm="24" :md="12" :lg="12" :xl="12">

				<Left></Left>

			</el-col>
			<el-col :xs="24" :sm="24" :md="12" :lg="12" :xl="12">
				<Right></Right>
			</el-col>
		</el-row>
		<!-- <div class="main">
	  <Left class="left"></Left>
	  <Right class="right"></Right>
  </div> -->
		<el-row :gutter="10">
			<el-col :span="24">
				<Nav></Nav>
			</el-col>
		</el-row>
		<!-- <div class="footer">
      左手文件系统 &copy; 2024 仿Windows文件系统
  </div> -->
	</el-watermark>
</template>

<style>
	body {
		font-family: '微软雅黑', sans-serif;
		background-color: #f0f0f0;
		background-image: url("https://win12online.com/background/bg-light.svg");
		background-size: cover;
	}

	.main {
		display: flex;
		margin: 20px;
	}

	.header {
		/*background-color: #3a7bd5;*/
		height: 60px;
		display: flex;
		align-items: center;
		justify-content: center;
		padding: 0 20px;
		opacity: 0.8;
	}

	.header h1 {
		color: black;
		margin: 0;
		font-size: 24px;
	}

	.main {
		display: flex;
		margin: 20px;
	}

	.footer {
		position: fixed;
		width: 100%;
		bottom: 0;
		/*background-color: #3a7bd5;*/
		height: 60px;
		display: flex;
		align-items: center;
		justify-content: center;
		color: white;
		font-size: 14px;
	}
</style>
