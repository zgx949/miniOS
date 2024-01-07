<template>
  <el-table
      :data="filterTableData"
      style="width: 100%; color: #000000;"
      height="300"
      :header-cell-style="{ color: '#000000' }"
  >
    <el-table-column label="文件名" prop="fileName" width="300">
      <template #default="scope">
        <el-button v-if="scope.row.fileType==='folder'" link style="color: #000000;" @click="open(scope.row)">
          <el-icon color="#67C23A"><Folder /></el-icon>
          {{ scope.row.fileName }}
        </el-button>
        <el-button v-else link style="color: #000000;" @click="open(scope.row)">
          <el-icon color="#409EFF"><Document /></el-icon>
          {{ scope.row.fileName }}
        </el-button>
      </template>
    </el-table-column>

    <el-table-column label="修改日期" prop="modificationTime" width="120" />
    <el-table-column label="类型" prop="fileType" width="80">
      <template #default="scope">
        <el-tag type="success" v-if="scope.row.fileType === 'folder'">文件夹</el-tag>
        <el-tag v-else>文件</el-tag>
      </template>
    </el-table-column>
    <el-table-column label="大小" prop="fileSize"  width="100"/>
    <el-table-column align="right">
      <template #header>
        <el-input v-model="search" placeholder="搜索文件(夹)" />
      </template>
      <template #default="scope">
        <el-button size="small" type="success" @click="handleDelete(scope.$index, scope.row)">分享</el-button>
        <el-button size="small" type="primary" @click="handleDelete(scope.$index, scope.row)">下载</el-button>
        <el-button size="small" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
      </template>
    </el-table-column>
  </el-table>
</template>

<script setup>
import {defineEmits , defineProps, onMounted, ref, computed} from 'vue'
const emits = defineEmits(['openFolder'])
import {ElNotification} from "element-plus";
import {
  Folder,
  Document,
} from '@element-plus/icons-vue'

const tableData =  defineProps({
  data: Array
})

onMounted(() => {
  filterTableData.value = tableData.value
})

// 搜索的文件内容
const search = ref('')

// 表格数据计算
const filterTableData = computed(() =>

    tableData.data.filter(
        (data) =>
            !search.value ||
            data.fileName.toLowerCase().includes(search.value.toLowerCase())
    )
)
const handleDelete = (index, row) => {
  ElNotification({
    title: 'Success',
    message: 'This is a success message',
    type: 'success',
  })
  console.log(index, row)
}


// 定义一个方法用于触发事件并携带数据
const emitValue = () => {
  // 假设这里的数据是动态的，从某个地方获取
  const valueToEmit = 'Hello from child component'

}

// 打开文件或者文件夹
const open = (row) => {
  if (row.fileType === 'folder') {
    // 改变当前路径ID
    emits('openFolder', row._id)

    return
  }

  ElNotification({
    title: '文件系统',
    message: `打开文件：${row.fileName}`,
    type: 'success',
  })


}
</script>

<style scoped>

</style>