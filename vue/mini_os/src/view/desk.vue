<script setup>
import { ref, onMounted, onBeforeMount } from "vue";
import Apps from '@/components/Apps.vue'
import Nav from '@/components/Nav.vue'
import { ElNotification, ElLoading } from "element-plus";
// 加载完成
const loaded = () => {
  loading.close()
  ElNotification({
    title: '系统提示',
    message: `本次开机用时：${startTime}ms`,
    type: 'success',
  })
}
const openList = ref(null)
var loading = null
var startTime = 0
var timer = null

onBeforeMount(() => {
  loading = ElLoading.service({
    lock: true,
    text: '正在加载APP',
    background: 'rgba(0, 0, 0, 0.7)',
  })
  timer = setInterval(() => {
    startTime++
  }, 1)
})

// 打开的应用发生变化
const openAppChange = (data) => {
  openList.value = data
}
// 最大化APP
const appsRef = ref(null)
const showApp = (index)=> {
  // 向Apps组件发起调用最大化窗口
  appsRef.value.show(index)
}

onMounted(() => {

})


</script>

<template>
  <div class="header">
    <h3>左手网盘-Windows13版</h3>
  </div>

  <el-row :gutter="10">
    <el-col :xs="24" :sm="24" :md="24" :lg="24" :xl="24">
      <Apps @loaded="loaded" @openAppChange="openAppChange" ref="appsRef"></Apps>
    </el-col>
  </el-row>

  <el-row>
    <div class="fixed-bottom">
      <Nav :openList="openList" @show="showApp"></Nav>
    </div>
  </el-row>

</template>

<style>
body {
  font-family: '微软雅黑', sans-serif;
  background-color: #f0f0f0;
  background-image: url("/bg-light.svg");
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
