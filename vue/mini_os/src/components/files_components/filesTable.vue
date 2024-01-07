<template>
  <el-table
      :data="filterTableData"
      style="width: 100%; color: #000000;"
      height="400"
      :header-cell-style="{ color: '#000000' }"
  >
    <el-table-column label="文件名" prop="fileName" width="250">
      <template #default="scope">
        <el-button v-if="scope.row.fileType==='folder'" link style="color: #000000;" @click="open(scope.row)">
          <span class="fileicon">
            <el-icon color="#67C23A">
              <svg t="1704633233498" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="2842" width="200" height="200"><path d="M848.8576 199.1936H415.7568c0-26.5728-21.5424-48.128-48.128-48.128H175.1424c-26.5728 0-48.128 21.5424-48.128 48.128V343.5648c0 26.5984 21.5424 48.1408 48.128 48.1408h673.728c26.5728 0 48.128-21.5424 48.128-48.1408v-96.2432c-0.0128-26.5856-21.5552-48.128-48.1408-48.128z" fill="#CCA352" p-id="2843"></path><path d="M800.7424 247.3088H223.2576c-26.5728 0-48.128 21.5424-48.128 48.128v48.128c0 26.5984 21.5424 48.1408 48.128 48.1408h577.472c26.5728 0 48.128-21.5424 48.128-48.1408v-48.128c0-26.5728-21.5424-48.128-48.1152-48.128z" fill="#FFFFFF" p-id="2844"></path><path d="M848.8576 295.4368H175.1424c-26.5728 0-48.128 21.5424-48.128 48.128v481.2544c0 26.5472 21.5424 48.128 48.128 48.128h673.728c26.5728 0 48.128-21.568 48.128-48.128V343.552c-0.0128-26.5728-21.5552-48.1152-48.1408-48.1152z" fill="#FFCC66" p-id="2845"></path></svg>
            </el-icon>
          </span>
          <h3 class="filename">{{ scope.row.fileName }}</h3>
        </el-button>
        <el-button v-else link style="color: #000000; " @click="open(scope.row)">
          <span class="fileicon">
            <el-icon color="#409EFF">
              <svg t="1704633352014" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="9482" width="200" height="200"><path d="M512 512m-448 0a448 448 0 1 0 896 0 448 448 0 1 0-896 0Z" fill="#55A7F7" p-id="9483"></path><path d="M256 256m64 0l384 0q64 0 64 64l0 384q0 64-64 64l-384 0q-64 0-64-64l0-384q0-64 64-64Z" fill="#E2BF7A" p-id="9484"></path><path d="M332 302h360v420H332z" fill="#FFFFFF" p-id="9485"></path><path d="M322 342h380v360H322z" fill="#E9EBF1" p-id="9486"></path><path d="M302 382h420v300H302z" fill="#FFFFFF" p-id="9487"></path><path d="M282 422h460v300H282z" fill="#E9EBF1" p-id="9488"></path><path d="M768 412.192V704c0 35.346-28.654 64-64 64H320c-35.346 0-64-28.654-64-64V412.187a32 32 0 0 0 15.27 27.278C380.543 506.488 460.787 540 512 540c51.212 0 131.456-33.512 240.73-100.535A32 32 0 0 0 768 412.192z" fill="#FFD786" p-id="9489"></path><path d="M512 604m-32 0a32 32 0 1 0 64 0 32 32 0 1 0-64 0Z" fill="#CBA559" p-id="9490"></path></svg>
            </el-icon>
          </span>
          <h3 class="filename">{{ scope.row.fileName }}</h3>
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
        <el-button size="small" type="success" @click="handleShare(scope.$index, scope.row)">分享</el-button>
        <el-button size="small" type="primary" @click="handleDownload(scope.$index, scope.row)" :disabled="scope.row.fileType === 'folder'">下载</el-button>
        <el-button size="small" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
      </template>
    </el-table-column>
  </el-table>
</template>

<script setup>
import {defineEmits , defineProps, onMounted, ref, computed} from 'vue'
const emits = defineEmits(['openFolder', 'reload'])
import {ElNotification} from "element-plus";
import {
  Folder,
  Document,
} from '@element-plus/icons-vue'
import {delFCB} from "@/api/files";

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

// 删除文件
const handleDelete = (index, row) => {
  delFCB(row._id).then(res => {
    ElNotification({
      title: '文件系统',
      message: `${res.data.msg}\n删除文件数量：${res.data.data.DeletedCount}`,
      type: 'warning',
    })
    // 刷新数据
    emits('reload')
  })

}

// 分享文件
const handleShare = (index, row) => {
  ElNotification({
    title: '文件系统',
    message: '分享文件',
    type: 'success',
  })
  console.log(index, row)
}

// 下载文件
const handleDownload = (index, row) => {
  ElNotification({
    title: '文件系统',
    message: '正在获取下载链接',
    type: 'info',
  })
  console.log(index, row)
}


// 打开文件或者文件夹
const open = (row) => {
  if (row.fileType === 'folder') {
    // 改变当前路径ID
    emits('openFolder', row._id, row.fileName)

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
/* 文件名 */
.filename {
  white-space: normal;
  word-break: break-all;
  overflow-wrap: break-word;
  text-align: left;
}
/* 文件图标 */
.fileicon {
  font-size: 40px;
}
</style>