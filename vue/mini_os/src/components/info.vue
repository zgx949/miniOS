<template>
  信息
  <el-row>
    <el-col :xs="24" :sm="12" :md="6" :lg="6">
      <el-card class="card">
        <div class="demo-progress">
          <h4>磁盘限制</h4>
        <el-progress type="dashboard" :percentage="percentage" :color="colors" />
        <div>
          <el-button-group>
            <el-button :icon="Minus" @click="decrease" />
            <el-button :icon="Plus" @click="increase" />
          </el-button-group>
        </div>
      </div>
      </el-card>
    </el-col>
    <el-col :xs="24" :sm="12" :md="6" :lg="6">
      <el-card class="card">
        <div class="demo-progress">
          <h4>CPU占比</h4>
        <el-progress type="dashboard" :percentage="percentage2" :color="colors" />
      </div>
      </el-card>
    </el-col>
    <el-col :xs="24" :sm="12" :md="6" :lg="6">
      <el-card class="card">
        <div class="demo-progress">
          <el-progress :percentage="50">
            <el-button text>内存清理🧹</el-button>
          </el-progress>
          <el-progress
            :text-inside="true"
            :stroke-width="20"
            :percentage="50"
            status="exception"
          >
            <span>磁盘已用</span>
          </el-progress>
          <el-progress type="circle" :percentage="100" status="success">
            <el-button type="success" :icon="Check" circle/>
          </el-progress>
          <el-progress type="dashboard" :percentage="80">
            <template #default="{ percentage }">
              <span class="percentage-value">{{ percentage }}%</span>
              <span class="percentage-label">进程阻塞</span>
            </template>
          </el-progress>
        </div>
      </el-card>
    </el-col>
    <el-col :xs="24" :sm="12" :md="6" :lg="6">
      <el-card class="card">
        <div class="demo-progress">
          <el-progress :percentage="50" :stroke-width="15" striped />
          <el-progress
            :percentage="30"
            :stroke-width="15"
            status="warning"
            striped
            striped-flow
          />
          <el-progress
            :percentage="100"
            :stroke-width="15"
            status="success"
            striped
            striped-flow
            :duration="10"
          />
          <el-progress
            :percentage="percentage"
            :stroke-width="15"
            status="exception"
            striped
            striped-flow
            :duration="duration"
          />
          <el-button-group>
            <el-button :icon="Minus" @click="decrease" />
            <el-button :icon="Plus" @click="increase" />
          </el-button-group>
        </div>
      </el-card>
    </el-col>
  </el-row>

</template>

<script lang="ts" setup>
import {computed, onMounted, ref} from 'vue'
import { Minus, Plus } from '@element-plus/icons-vue'

const percentage = ref(10)
const percentage2 = ref(0)
const duration = computed(() => Math.floor(percentage.value / 10))
const decrease = () => {
  percentage.value -= 10
  if (percentage.value < 0) {
    percentage.value = 0
  }
}
const colors = [
  { color: '#f56c6c', percentage: 20 },
  { color: '#e6a23c', percentage: 40 },
  { color: '#5cb87a', percentage: 60 },
  { color: '#1989fa', percentage: 80 },
  { color: '#6f7ad3', percentage: 100 },
]

const increase = () => {
  percentage.value += 10
  if (percentage.value > 100) {
    percentage.value = 100
  }
}
onMounted(() => {
  setInterval(() => {
    percentage2.value = (percentage2.value % 100) + 10
  }, 500)
})
</script>
<style scoped>
.card {
  padding: 10px;
  margin: 10px;
  height: 80%;
}
.demo-progress .el-progress--line {
  margin-bottom: 15px;
  max-width: 600px;
}
.demo-progress .el-progress--circle {
  margin-right: 15px;
}
.demo-progress .el-progress--line {
  margin-bottom: 15px;
  max-width: 600px;
}
</style>