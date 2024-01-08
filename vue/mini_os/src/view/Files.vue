<template>
	<div class="files">

		<div style="background-color: #ffffff">
			<el-text style="color: #000000; font-size: large;">当前目录: </el-text>
      <span style="color: #000000">{{ path }}</span>
      <!-- 操作菜单   -->
      <fileOperation @back="back" @create="create" :folderId="parentId.at(-1)" @reload="reload"></fileOperation>
		</div>
		<!-- 文件表格数据 -->
    <filesTable :data="tableData" @openFolder="openFolder" @reload="reload" v-loading="loading"></filesTable>
	</div>


</template>

<script setup>
import fileOperation from '@/components/files_components/fileOperation.vue'
import filesTable from '@/components/files_components/filesTable.vue'
import {computed, ref, onMounted, watch, defineEmits} from 'vue'
const emits = defineEmits(["loaded"])
import { ElNotification } from 'element-plus'
import {createFCB, list} from "@/api/files";
const dialogFormVisible = ref(false)

const pathArr = ref(['root'])

const path = computed(() => {
  return pathArr.value.join('/')
})
const options = []

const loading = ref(false)

const openFolder = (id, dirName)=> {
  parentId.value.push(id)
  // 把当前目录名加入数组
  pathArr.value.push(dirName)
  loadData(parentId.value.at(-1))
}

const tableData = ref([
  {
    "_id": "65994c104379f4da38c8e221",
    "creationTime": "0001-01-01T00:00:00Z",
    "fileLocation": 0,
    "fileName": "123.txt",
    "fileSize": 0,
    "fileType": "file",
    "group": 0,
    "inodeNumber": 0,
    "modificationTime": "0001-01-01T00:00:00Z",
    "owner": 0,
    "parentId": "65994c2c4379f4da38c8e222",
    "permissions": ""
  }
]) // 文件目录
const parentId = ref(["root"]) // 文件夹id队列

// 监听文件夹id
watch(parentId, () =>{
  loadData(parentId.value.at(-1))
})

// 刷新数据
const reload = () => {
  loadData(parentId.value.at(-1))
}

// 加载数据
const loadData = (id) => {
  loading.value = true
  list(id).then(res => {
    let data = res.data.data
    // 加载数据
    if (res.data.code === 0) {
      if (!data) {
        data = []
      }
      data.sort((a, b) => b.fileType.localeCompare(a.fileType))
      tableData.value = data
    }
    loading.value = false

  })
}
// 后退文件夹
const back = () => {
  // 删除一个文件名

  const id = parentId.value.at(-1)
  if (id === 'root') {
    ElNotification({
      title: '文件系统',
      message: '已经是根目录了',
      type: 'error',
    })
    return
  }
  pathArr.value.pop()
  parentId.value.pop()

  loadData(parentId.value.at(-1))
}

// 创建一个FCB
const create = (FileName, FileType) => {
  let id = parentId.value.at(-1)
  if (id === 'root') {
    id = null
  }
  createFCB({
    FileName: FileName,
    FileType: FileType,
    parentId: id
  }).then(res => {
    if (res.data.code === 0) {
      dialogFormVisible.value = false
      ElNotification({
        title: '文件系统',
        message: res.data.msg,
        type: 'success',
      })
      loadData(parentId.value.at(-1))

    } else {
      ElNotification({
        title: '文件系统',
        message: res.data.msg,
        type: 'error',
      })
    }
  })
}

onMounted(() => {
  loadData(parentId.value[0])

})


</script>

<style scoped>

</style>
