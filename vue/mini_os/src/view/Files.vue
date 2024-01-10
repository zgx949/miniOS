<template>
	<div class="files">

		<div style="background-color: #ffffff">
			<el-text style="color: #000000; font-size: large;">当前目录: </el-text>
      <span style="color: #000000">{{ path }}</span>
      <!-- 操作菜单   -->
      <fileOperation @back="back" @create="create" :folderId="parentId.at(-1)" @reload="reload"></fileOperation>
		</div>
		<!-- 文件表格数据 -->
    <filesTable :data="tableData" @openFolder="openFolder" @reload="reload" v-loading="loading" @openFile="openFile"></filesTable>
	</div>


</template>

<script setup>
import fileOperation from '@/components/files_components/fileOperation.vue'
import filesTable from '@/components/files_components/filesTable.vue'
import {computed, ref, onMounted, watch, defineEmits} from 'vue'
const emits = defineEmits(["loaded", "openFile"])
import { ElNotification } from 'element-plus'
import {createFCB, list} from "@/api/files";
import {getOpenUrl} from "../api/files";
import {getRootUrl} from "../utils/utils";
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

const openFile = (file)=> {
  // 发送打开文件消息，要求创建新的窗口 TODO: 可能要改成文件的下载地址，加入文件名
  const fileURL = getRootUrl() + getOpenUrl(file.id)
  emits('openFile', {
    name: file.file_name,
    img: '<svg t="1704633352014" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="9482" width="200" height="200"><path d="M512 512m-448 0a448 448 0 1 0 896 0 448 448 0 1 0-896 0Z" fill="#55A7F7" p-id="9483"></path><path d="M256 256m64 0l384 0q64 0 64 64l0 384q0 64-64 64l-384 0q-64 0-64-64l0-384q0-64 64-64Z" fill="#E2BF7A" p-id="9484"></path><path d="M332 302h360v420H332z" fill="#FFFFFF" p-id="9485"></path><path d="M322 342h380v360H322z" fill="#E9EBF1" p-id="9486"></path><path d="M302 382h420v300H302z" fill="#FFFFFF" p-id="9487"></path><path d="M282 422h460v300H282z" fill="#E9EBF1" p-id="9488"></path><path d="M768 412.192V704c0 35.346-28.654 64-64 64H320c-35.346 0-64-28.654-64-64V412.187a32 32 0 0 0 15.27 27.278C380.543 506.488 460.787 540 512 540c51.212 0 131.456-33.512 240.73-100.535A32 32 0 0 0 768 412.192z" fill="#FFD786" p-id="9489"></path><path d="M512 604m-32 0a32 32 0 1 0 64 0 32 32 0 1 0-64 0Z" fill="#CBA559" p-id="9490"></path></svg>',
    url: `https://view.xdocin.com/view?src=${encodeURIComponent(fileURL)}`,
    component: '',
    width: '90%',
    dialogVisible: true,
    opened: true
  })
}

const tableData = ref([
  {
    "file_name": "视频",
    "file_size": 0,
    "parent_id": 1,
    "creation_time": null,
    "modification_time": null,
    "permissions": null,
    "owner": 0,
    "group": 0,
    "file_type": "folder",
    "id": 12
  },
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
      data.sort((a, b) => b.file_type.localeCompare(a.file_type))
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
