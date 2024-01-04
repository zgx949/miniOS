<script setup>
import { ref, onMounted, onBeforeMount } from "vue";
import Right from './components/Right.vue'
import Nav from './components/Nav.vue'
import { ElNotification, ElLoading } from "element-plus";
const fullscreenLoading = ref(true)  // 全屏加载

var loading = null
var startTime = 0
var timer = null
onBeforeMount(() => {
  loading = ElLoading.service({
    lock: true,
    text: 'Loading',
    background: 'rgba(0, 0, 0, 0.7)',
  })
  timer = setInterval(() => {
    startTime++
  }, 1)
})


onMounted(() => {

  setTimeout(()=> {
    loading.close()
    clearInterval(timer)
    ElNotification({
      title: '系统提示',
      message: `本次开机用时：${startTime}ms`,
      type: 'success',
    })
  }, 500)
})


</script>

<template>

<!--	<el-watermark :font="font" :content="['左手文件系统']">-->


		<div class="header">
			<h1>左手网盘-Windows13版</h1>
		</div>

		<el-row :gutter="10">
			<el-col :xs="24" :sm="24" :md="24" :lg="24" :xl="24">
        <Right></Right>
			</el-col>

		</el-row>

    <el-row>
      <div class="fixed-bottom"><Nav></Nav></div>
    </el-row>

<!--	</el-watermark>-->
</template>

<style>
	body {
		font-family: '微软雅黑', sans-serif;
		background-color: #f0f0f0;
		background-image: url("https://win12online.com/background/bg-light.svg");
		background-size: cover;
  }
  .fixed-bottom {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    padding: 10px;
    text-align: center;

  }

	.header {
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
