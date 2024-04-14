<template>
<h1>开始</h1>
<el-row>
  <el-col :span="8">
    <el-countdown title="Start to grab" :value="value" />
  </el-col>
  <el-col :span="8">
    <el-countdown
      title="Remaining VIP time"
      format="HH:mm:ss"
      :value="value1"
    />
    <el-button class="countdown-footer" type="primary" @click="reset"
      >Reset
    </el-button>
  </el-col>
  <el-col :span="8">
    <el-countdown format="DD [days] HH:mm:ss" :value="value2">
      <template #title>
        <div style="display: inline-flex; align-items: center">
          <el-icon style="margin-right: 4px" :size="12">
            <Calendar />
          </el-icon>
          Still to go until next month
        </div>
      </template>
    </el-countdown>
    <div class="countdown-footer">{{ value2.format('YYYY-MM-DD') }}</div>
  </el-col>
</el-row>

<el-row>
  <el-col :span="6">
    <el-statistic title="Daily active users" :value="268500" />
  </el-col>
  <el-col :span="6">
    <el-statistic :value="138">
      <template #title>
        <div style="display: inline-flex; align-items: center">
          Ratio of men to women
          <el-icon style="margin-left: 4px" :size="12">
            <Male />
          </el-icon>
        </div>
      </template>
      <template #suffix>/100</template>
    </el-statistic>
  </el-col>
  <el-col :span="6">
    <el-statistic title="Total Transactions" :value="outputValue" />
  </el-col>
  <el-col :span="6">
    <el-statistic title="Feedback number" :value="562">
      <template #suffix>
        <el-icon style="vertical-align: -0.125em">
          <ChatLineRound />
        </el-icon>
      </template>
    </el-statistic>
  </el-col>
</el-row>

<el-row :gutter="16">
    <el-col :span="8">
      <div class="statistic-card">
        <el-statistic :value="98500">
          <template #title>
            <div style="display: inline-flex; align-items: center">
              Daily active users
              <el-tooltip
                effect="dark"
                content="Number of users who logged into the product in one day"
                placement="top"
              >
                <el-icon style="margin-left: 4px" :size="12">
                  <Warning />
                </el-icon>
              </el-tooltip>
            </div>
          </template>
        </el-statistic>
        <div class="statistic-footer">
          <div class="footer-item">
            <span>than yesterday</span>
            <span class="green">
              24%
              <el-icon>
                <CaretTop />
              </el-icon>
            </span>
          </div>
        </div>
      </div>
    </el-col>
    <el-col :span="8">
      <div class="statistic-card">
        <el-statistic :value="693700">
          <template #title>
            <div style="display: inline-flex; align-items: center">
              Monthly Active Users
              <el-tooltip
                effect="dark"
                content="Number of users who logged into the product in one month"
                placement="top"
              >
                <el-icon style="margin-left: 4px" :size="12">
                  <Warning />
                </el-icon>
              </el-tooltip>
            </div>
          </template>
        </el-statistic>
        <div class="statistic-footer">
          <div class="footer-item">
            <span>month on month</span>
            <span class="red">
              12%
              <el-icon>
                <CaretBottom />
              </el-icon>
            </span>
          </div>
        </div>
      </div>
    </el-col>
    <el-col :span="8">
      <div class="statistic-card">
        <el-statistic :value="72000" title="New transactions today">
          <template #title>
            <div style="display: inline-flex; align-items: center">
              New transactions today
            </div>
          </template>
        </el-statistic>
        <div class="statistic-footer">
          <div class="footer-item">
            <span>than yesterday</span>
            <span class="green">
              16%
              <el-icon>
                <CaretTop />
              </el-icon>
            </span>
          </div>
          <div class="footer-item">
            <el-icon :size="14">
              <ArrowRight />
            </el-icon>
          </div>
        </div>
      </div>
    </el-col>
  </el-row>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import dayjs from 'dayjs'
import { useTransition } from '@vueuse/core'
import { Calendar, ChatLineRound, Male,ArrowRight, CaretBottom, CaretTop, Warning, } from '@element-plus/icons-vue'

const value = ref(Date.now() + 1000 * 60 * 60 * 7)
const value1 = ref(Date.now() + 1000 * 60 * 60 * 24 * 2)
const value2 = ref(dayjs().add(1, 'month').startOf('month'))

function reset() {
  value1.value = Date.now() + 1000 * 60 * 60 * 24 * 2
}
const source = ref(0)
const outputValue = useTransition(source, {
  duration: 1500,
})
source.value = 172000
</script>

<style scoped>
:global(h2#card-usage ~ .example .example-showcase) {
  background-color: var(--el-fill-color) !important;
}

.el-statistic {
  --el-statistic-content-font-size: 28px;
}

.statistic-card {
  height: 100%;
  padding: 20px;
  border-radius: 4px;
  background-color: var(--el-bg-color-overlay);
}

.statistic-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  font-size: 12px;
  color: var(--el-text-color-regular);
  margin-top: 16px;
}

.statistic-footer .footer-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.statistic-footer .footer-item span:last-child {
  display: inline-flex;
  align-items: center;
  margin-left: 4px;
}

.green {
  color: var(--el-color-success);
}
.red {
  color: var(--el-color-error);
}
</style>