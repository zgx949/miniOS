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
            <el-button type="success" class="button" @click="install(app.id)" :icon="Download">
            </el-button>
          </div>
        </div>
      </el-card>
    </el-col>
  </el-row>
</template>

<script setup>
import {onMounted, ref, defineEmits} from 'vue'
const emits = defineEmits(["reloadDesk"])
import {InstallApp, MarketApp} from "@/api/apps";
import { Download } from "@element-plus/icons-vue"
import {ElNotification} from "element-plus";

const apps = ref([])

onMounted(() => {
  MarketApp().then(res => {
    if (res.data.code === 0) {
      apps.value = res.data.data
    }
  })
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
  })
  emits("reloadApps")
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