<script setup>
import { ref, onMounted, onBeforeMount } from "vue";
import Apps from '@/components/Apps.vue'
import Nav from '@/components/Nav.vue'
import { ElNotification, ElLoading } from "element-plus";
// 加载完成
const loaded = () => {
  loading.close()
  // 计算开机时间
  ElNotification({
    title: '系统提示',
    message: `开机时间：${(performance.now() - startTime).toFixed(2)}ms`,
    type: 'success'
  })

}
const openList = ref(null)
var loading = null
var startTime = performance.now()

onBeforeMount(() => {
  loading = ElLoading.service({
    lock: true,
    text: '正在加载APP',
    background: 'rgba(0, 0, 0, 0.7)',
  })
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
  <div class="image-kun-layer">
  </div>
  <div class="header">
    <h3>Windows-Kun版</h3>
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
/* 坤层图片 */
.image-kun-layer {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url('/cxk.jpg'); /* 替换为你的图片URL */
  background-size: cover;
  opacity: 0.1; /* 调整这个值以改变透明度，0代表完全透明，1代表不透明 */
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
  position: fixed;
  top: 0;
  /*left: 50%;*/
  right: 0px;
  padding: 10px;
  /*transform: translateX(-50%);*/
  opacity: 0.5;
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
