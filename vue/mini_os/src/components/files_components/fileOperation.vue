<template>
  <!-- 新建文件窗口 -->
  <el-dialog v-model="dialogFormVisible" title="新建文件/文件夹" width="80%">
    <el-radio-group v-model="newFileType">
      <el-radio :label="'folder'">文件夹</el-radio>
      <el-radio :label="'file'">文件</el-radio>
    </el-radio-group>
    文件（夹）名<el-input v-model="createDirName"></el-input>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取消</el-button>
        <el-button type="primary" @click="create(createDirName, newFileType)">
          新建
        </el-button>
      </span>
    </template>
  </el-dialog>

  <!-- 上传文件窗口 -->
  <el-dialog v-model="dialogUploadVisible" title="上传文件" width="80%">
    <el-upload
        class="upload-demo"
        drag
        multiple
        v-model:file-list="fileList"
        :auto-upload="false"
        :on-change="handleChange"
    >
      <el-icon class="el-icon--upload"><upload-filled /></el-icon>
      <div class="el-upload__text">
        拖到此处 或 <em>选择文件</em>
      </div>
      <template #tip>
        <div class="el-upload__tip">
          不限制文件和大小，支持断点续传
        </div>
      </template>
    </el-upload>

    <el-table :data="tableData" stripe style="width: 100%">
      <el-table-column prop="name" label="名字"/>
      <el-table-column prop="percentage" label="进度">
        <template #default="scope">
          <el-progress :text-inside="true" :stroke-width="26" :percentage="scope.row.percentage" />
        </template>
      </el-table-column>
    </el-table>
  </el-dialog>

  <!-- 操作面版 -->
  <div>
    <el-row :gutter="10">
      <el-col :xs="12" :sm="12" :md="6" :lg="6" :xl="6">
        <div @click="back">
          <el-button color="#C45DD5" class="fop" type="primary" :icon="ArrowLeftBold"><span
              style="color: #ffffff;">后退</span>
          </el-button>
        </div>

      </el-col>
      <el-col :xs="12" :sm="12" :md="6" :lg="6" :xl="6">
        <div @click="dialogUploadVisible = true">
          <el-button color="#C45DD5" class="fop" type="primary" :icon="UploadFilled"><span
              style="color: #ffffff;">上传</span>
          </el-button>
        </div>
      </el-col>
      <el-col :xs="12" :sm="12" :md="6" :lg="6" :xl="6">
        <div @click="dialogFormVisible=true">
          <el-button color="#C45DD5" class="fop" type="primary" :icon="DocumentAdd"><span
              style="color: #ffffff;">新建</span></el-button>
        </div>
      </el-col>
      <el-col :xs="12" :sm="12" :md="6" :lg="6" :xl="6">
        <div @click="emits('reload')">
          <el-button color="#C45DD5" class="fop" type="primary" :icon="Files"><span
              style="color: #ffffff;">刷新</span>
          </el-button>
        </div>
      </el-col>

    </el-row>
  </div>
</template>

<script setup>
import {
  Files,
  ArrowLeftBold,
  UploadFilled,
  DocumentAdd
} from '@element-plus/icons-vue'

const chunkSize = 1024*1024*1 // 文件块大小1MB

import {defineEmits, ref, defineProps} from 'vue'
const props = defineProps({
  folderId: String // 文件夹id
})
import {createFCB, upload} from "@/api/files"
import {ElNotification} from "element-plus"
import {buildChunkForm, getChunkCount, getFileMd5} from "@/utils/utils";
const emits = defineEmits(['back', 'create', 'reload'])

const newFileType = ref('folder') // 创建文件还是文件夹

const createDirName = ref('') // 新建文件名

const tableData = ref([]) // 上传文件列表信息

const fileList = ref([]) // 上传文件列表


const back = () => {
  emits('back')
}
// 新建弹窗
const dialogFormVisible = ref(false)

// 上传文件弹窗
const dialogUploadVisible = ref(false)

// 创建一个FCB
const create = (FileName, FileType) => {
  emits('create', FileName, FileType)
  dialogFormVisible.value = false
}


/**
 * 将分块文件上传至服务器
 * @param fcbId
 * @param file 上传的分块文件
 * @param chunkNumber 当前是第几块
 * @param chunkTotal 文件分块的总数
 * @param fileName 文件名称
 */
const uploadFileToServer = async (fcbId, file, chunkNumber, chunkTotal, fileName) => {
  // 构造表单
  const form = await buildChunkForm(fcbId, file, chunkNumber, chunkTotal, fileName);
  let result = await upload(form)
  return result
}

/**
 * el-upload内置的change函数，文件上传或者上传成功时的回调，不过这里因为
 * :auto-upload="false"的缘故，上床成功的回调不会执行
 * @param uploadFile el-upload当前上传的文件对象
 * @param uploadFiles el-upload上传的文件列表
 */
const handleChange = async (uploadFile, uploadFiles) => {

  const res = await createFCB({
    FileName: uploadFile.name,
    FileType: 'file',
    parentId: props.folderId === 'root' ? null : props.folderId,
    FileSize: uploadFile.size
  })
  // debugger
  if (res.data.code !== 0) {
    // FCB 创建失败
    ElNotification({
      title: '文件系统',
      message: res.data.msg,
      type: 'error',
    })
    return
  }

  // debugger
  // FCB 创建成功
  const fid = res.data.data.id

  tableData.value.push({...uploadFile})

  const index = tableData.value.findIndex(item => item.uid === uploadFile.uid)

  let fileName = uploadFile.name


  const fileSize = uploadFile.size || 0
  // 计算文件分块的总数
  let chunkTotals = getChunkCount(uploadFile) // 文件分块的总数
  let errorList = [] // 上传失败的文件块
  let successCount = 0 // 上传成功的文件块
  if (chunkTotals > 0) {
    // 上传文件分块
    for (let chunkNumber = 0, start = 0; chunkNumber < chunkTotals; chunkNumber++,  start += chunkSize) {
      let end = Math.min(fileSize, start + chunkSize);
      // 切片

      const files = uploadFile.raw?.slice(start, end)
      // 多线程上传
      const result = await uploadFileToServer(fid, files, chunkNumber+1, chunkTotals, fileName)
      if (result.error) {
        // 上传失败
        errorList.push({
          fid: fid,
          files: files,
          chunkNumber: chunkNumber + 1,
          chunkTotals: chunkTotals,
          fileName: fileName
        })
        continue
      }
      successCount++
      const percents = (successCount / chunkTotals * 100).toFixed(2)
      uploadFile.percentage = percents
      tableData.value[index].percentage = percents
      console.log(result.data)
    }
  }
  // 重传失败的文件块
  while (errorList.length !== 0) {
    // 从队头取出一个文件块
    const error = errorList.shift()
    const result = await uploadFileToServer(error.fid, error.files, error.chunkNumber, error.chunkTotals, error.fileName)
    if (result.error) {
      // 上传失败
      errorList.push({
        fid: error.fid,
        files: error.files,
        chunkNumber: error.chunkNumber,
        chunkTotals: error.chunkTotals,
        fileName: error.fileName
      })
      continue
    }
    successCount++
    const percents = (successCount / chunkTotals * 100).toFixed(2)
    uploadFile.percentage = percents
    tableData.value[index].percentage = percents
    console.log(result.data)
  }

  emits('reload')
  console.log(uploadFiles)
}

</script>

<style scoped>
.fop {
  background-color: #C45DD5;
  border: none;
  color: white;
  text-align: center;
  text-decoration: none;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
  padding: 10px 24px;
  border-radius: 12px;
}

.fop:hover {
  /*background-color: #45a049;*/
  background-color: #8A66FE;
}
</style>