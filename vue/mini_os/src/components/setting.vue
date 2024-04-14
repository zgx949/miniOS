<template>
<!--<h5>设置</h5>-->
 <el-row class="tac">
  <el-col :span="4">
    <el-menu
      default-active="2"
      class="el-menu-vertical-demo"
      @open="handleOpen"
      @close="handleClose"
    >
      <el-sub-menu index="1">
        <template #title>
          <el-icon><location /></el-icon>
          <span>菜单1</span>
        </template>
        <el-menu-item-group title="应用组1">
          <el-menu-item index="1-1">设置1</el-menu-item>
          <el-menu-item index="1-2">设置2</el-menu-item>
        </el-menu-item-group>
        <el-menu-item-group title="分组2">
          <el-menu-item index="1-3">应用三</el-menu-item>
        </el-menu-item-group>
        <el-sub-menu index="1-4">
          <template #title>分组四</template>
          <el-menu-item index="1-4-1">应用</el-menu-item>
        </el-sub-menu>
      </el-sub-menu>
      <el-menu-item index="2">
        <el-icon><icon-menu /></el-icon>
        <span>Navigator Two</span>
      </el-menu-item>
      <el-menu-item index="3" disabled>
        <el-icon><document /></el-icon>
        <span>Navigator Three</span>
      </el-menu-item>
      <el-menu-item index="4">
        <el-icon><setting /></el-icon>
        <span>Navigator Four</span>
      </el-menu-item>
    </el-menu>
  </el-col>
  <el-col :span="20">
    <div style="height: 100%; width: 100%; background: rgba(255,255,255, 0.9);">
    </div>
  </el-col>
</el-row>
</template>

<script lang="ts" setup>
import {
  Document,
  Menu as IconMenu,
  Location,
  Setting,
} from '@element-plus/icons-vue'
const handleOpen = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
const handleClose = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
</script>

<style scoped>

</style>