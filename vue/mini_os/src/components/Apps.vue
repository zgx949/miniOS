<template>
  <div v-for="(app, i) in openList">
    <Window
        v-if="app.opened"
        v-model:model-value="app.dialogVisible"
        :width="app.width"
        :key="i"
        @closeWindow="closeWindow(i)"
        @hide="hide(i)"
    >
      <template v-slot:head>
        <span style="color: #000000; text-align: center">{{ app.name }}</span>
      </template>
      <div v-loading="loading" v-if="app.url !== ''">
        <iframe
            :src="app.url"
            ref="myIframe"
            frameborder="0"
            width="100%"
            style="display: block; height: 100vh;"
            @load="onIframeLoad"
          />
      </div>
      <Files v-else-if="app.component === 'Files'" @openFile="addWindow"></Files>
      <AppMarket v-else-if="app.component === 'AppMarket'" @reloadApps="loadData" />
    </Window>
  </div>

  <div class="desk">
    <div class="apps">
          <!-- 桌面应用展示 -->
            <div text plain :span="4" v-for="(item, i) in apps" class="app" :key="i" @click="open(item)">
              <div v-html="item.img"></div>
              <div class="name">{{ item.name }}</div>
            </div>
    </div>
<!--    <div v-for="(app, i) in openList">-->
<!--      <button @click="show(i)">{{app.name}}</button>-->
<!--    </div>-->
  </div>

</template>

<script setup>
import {ref, reactive, computed, watch, defineAsyncComponent, onMounted, defineEmits} from 'vue'
const emits = defineEmits(["loaded", "openAppChange"])
import Files from '@/view/Files.vue'
import { listApp } from '@/api/apps'
import Window from "@/components/window/window.vue";
import AppMarket from "@/view/AppMarket.vue";

const myIframe = ref(null)
const loading = ref(true) // 用于记录 iframe 是否已加载完成
const component = ref('Files')
// 已打开的应用列表
const openList = reactive([])

// 打开的应用发生了改变
watch(openList, ()=>{
  emits("openAppChange", openList)
})
// 计算浏览器高度
const innerHeight = ref(300)

const onIframeLoad = ()=> {
  loading.value = false // iframe 加载完成，将状态设置为 true
}

// 加载数据
const loadData = async ()=> {
  listApp().then(res => {
    if (res.data.code === 0) {
      apps.value = res.data.data
    }
  })
}

onMounted(() => {
  loadData().then(() => {
    for (let i = 0; i < apps.value.length; i++) {
      const item = apps.value[i]
      item['dialogVisible'] = false
      item['opened'] = false
    }
    // 发送加载完成
    emits("loaded", true)
  })

})

// app信息
const apps = ref([
  {
    name: '文件管理',
    img: '<svg t="1704374237567" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="6999" width="200" height="200"><path d="M352.644046 0C285.225208 0 225.205595 62.16671 225.205595 128.033032l-36.764903 0.924903C121.054885 128.957935 66.056175 190.183226 66.056175 256.066065v639.900903C66.056175 961.83329 126.075788 1024 193.478111 1024H671.207143c67.435355 0 127.438452-62.16671 127.438452-128.033032h31.876129c67.418839 0 127.421935-62.16671 127.421935-128.033033V281.500903a66.064516 66.064516 0 0 0-16.284903-43.437419L754.448434 23.601548a66.064516 66.064516 0 0 0-49.597936-22.627096L352.644046 0zM193.478111 959.983484c-33.428645 0-63.70271-31.347613-63.70271-64.016516V256.066065c0-47.549935 38.978065-64.016516 95.562323-64.016517v576c0 65.899355 60.003097 128.049548 127.438451 128.049549 0 0 345.269677-0.429419 382.414452-0.42942-0.115613 38.812903-25.368774 64.313806-63.983484 64.313807H193.478111z m254.728258-320.693678a31.95871 31.95871 0 0 1-31.859613-32.008258c0-17.672258 14.253419-32.008258 31.859613-32.04129h286.571355c17.606194 0.033032 31.859613 14.369032 31.876129 32.04129-0.016516 17.672258-14.269935 31.991742-31.876129 32.008258H448.222885z m-3.468387 134.936775A31.95871 31.95871 0 0 1 412.894885 742.218323c0-17.672258 14.253419-32.008258 31.843097-32.024775H731.325853c17.589677 0 31.859613 14.336 31.876129 32.024775-0.016516 17.672258-14.286452 31.991742-31.876129 32.008258H444.737982z m3.468387-261.698065a31.942194 31.942194 0 0 1-31.859613-32.008258c0-17.672258 14.269935-31.991742 31.859613-32.008258h286.571355c17.589677 0 31.859613 14.336 31.876129 32.008258-0.033032 17.672258-14.286452 31.991742-31.876129 32.008258H448.222885z m286.571355-320.478968V110.658065a16.516129 16.516129 0 0 1 29.200516-10.570323l107.486968 128.875355a16.516129 16.516129 0 0 1-12.684387 27.086451h-60.283871c-33.973677 0-63.719226-30.802581-63.719226-64z" fill="#2c2c2c" p-id="7000"></path></svg>',
    url: '',
    component: 'Files',
    width: '100%',
    dialogVisible: false,
    opened: false
  }
])

// 打开窗口
const open = (app)=> {
  let item = app
  item['dialogVisible'] = true
  item['opened'] = true
  console.log('打开app',item)
  openList.push(item)
}

// 关闭窗口
const closeWindow = (index) => {
  openList.splice(index, 1)
  loading.value = true
}

// 隐藏窗口
const hide = (index) => {
  openList[index].dialogVisible = false
}

// 显示窗口
const show = (index) => {
  openList[index].dialogVisible = true
}

// 对外提供接口
defineExpose({
  show
})

// 新增窗口调用
const addWindow = (app) => {
  openList.push(app)
}
</script>

<style>
.apps {
  margin-left: 1rem;
  display: flex;
  flex-wrap: wrap;
  align-content: stretch;
}

.app {

  text-align: center;
	border-radius: 30px;
	transition: box-shadow 0.3s ease; /* 添加过渡效果 */
  width: 100px;
  height: 100px;
  margin: 5px;
  float: left; /* 添加这一行 */

}

.app:hover {
	background-color: #f0f0f0; /* 设置app的背景颜色 */
	box-shadow: 0 20px 20px rgba(0, 0, 0, 0.1); /* 鼠标悬浮时添加阴影效果 */
}
.app:last-child {
	margin-right: 0; /* 移除最后一个app的右边距 */
}

.icon {
	width: 50px;
	height: 50px;
}
.name {
  color: #000000;
	font-size: 16px;
	font-weight: bold;
}

</style>