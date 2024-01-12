<template>
  <el-row :gutter="10" style="margin: 10px">
    <el-col
        v-for="(app, i) in apps"
        :key="i"
        :xs="24" :sm="12" :md="6" :lg="6" :xl="6"
    >
      <el-card :body-style="{ padding: '0px' }" class="card">
        <div v-html="app.img" class="image"></div>
        <div style="padding: 14px; text-align: center">
          <h3>{{ app.name }}</h3>
          {{ app.description }}
          <div class="bottom">
            <time class="time">{{ currentDate }}</time>
            <el-button v-if="!isInstalled(app.id)" type="success" class="button" @click="install(app.id)" :icon="Download">
            </el-button>
            <el-button v-else type="danger" class="button" @click="uninstall(app.id)" :icon="Delete">
            </el-button>
          </div>
        </div>
      </el-card>
    </el-col>
  </el-row>
</template>

<script setup>
import {onMounted, ref, defineEmits, watch} from 'vue'
const emits = defineEmits(["reloadDesk"])
import {InstallApp, MarketApp} from "@/api/apps";
import { Download, Delete } from "@element-plus/icons-vue"
import {ElNotification} from "element-plus";
import {listApp, UninstallApp} from "../api/apps";

const apps = ref([])
const installedAppsList = ref([])

const isInstalled = (id) => {
  return installedAppsList.value.some(item => item.id === id)
}

watch(apps, ()=>{
  listApp().then(res => {
    if (res.data.code === 0) {
      installedAppsList.value = res.data.data
    }
  })
})



const loadMarketApps = () => {
  MarketApp().then(res => {
    if (res.data.code === 0) {
      apps.value = res.data.data
    }
  })
}

onMounted(() => {
  loadMarketApps()

})


const install = (id) => {
  InstallApp(id).then(res => {
    if (res.data.code === 0) {
      ElNotification({
        title: '应用市场',
        message: res.data.msg,
        type: 'success'
      })
    } else {
      ElNotification({
        title: '应用市场',
        message: res.data.msg,
        type: 'info'
      })
    }
    loadMarketApps()
    emits("reloadApps")
  })
}

const uninstall = (id) => {
  if (id <= 2) {
    ElNotification({
      title: '应用市场',
      message: '系统应用无法卸载',
      type: 'info'
    })
    return
  }
  UninstallApp(id).then(res => {
    ElNotification({
        title: '应用市场',
        message: res.data.msg,
        type: res.data.code === 0?'success' : 'info'
    })
    loadMarketApps()
    emits("reloadApps")
  })
}
</script>

<style scoped>
.card {
  margin: 10px;
}
.time {
  font-size: 12px;
  color: #999;
}

.bottom {
  margin-top: 13px;
  line-height: 12px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.button {
  /*padding: 0;*/
  /*min-height: auto;*/
}

.image {
  text-align: center;
  padding: 14px;
}
</style>